"""Icons and illustrations through ``bc_gen`` (OpenAI or Gemini), keyed to alpha, cached.

Every prompt gets the house style: flat, minimal, two colours from the video's
palette on pure white, no text. Neither backend in bc-gen asks for a
transparent background, so the white is keyed out here: alpha is the distance
from white, and colour is un-premultiplied against white so anti-aliased edges
keep their true colour instead of a pale fringe. The result is trimmed to its
ink with an even margin and written as RGBA PNG (compositing) and WebP (review,
through ``bc_gen.to_webp``). The receipt is copied beside the asset.
"""

from __future__ import annotations

import asyncio
import shutil
from pathlib import Path

import numpy as np
from bc_gen import GeminiImage, GenCache, ImageRequest, OpenAIImage, generate_verified, to_webp
from PIL import Image

from . import CACHE, brand
from .spec import ImageSpec, Video

__all__ = ["DEFAULT_MODELS", "generate_images", "house_prompt", "key_white", "load_images"]

DEFAULT_MODELS = {"openai": "gpt-image-2.5-flare", "gemini": "gemini-3.1-flash-image"}


def house_prompt(spec: ImageSpec, theme: str) -> str:
    pal = brand.palette(theme)
    a, b = pal.known.upper(), pal.unknown.upper()
    if spec.kind == "icon":
        return (
            f"A flat, minimal, two-tone vector icon: {spec.prompt}. Use exactly two colours, "
            f"teal {a} and amber {b}, on a pure white #FFFFFF background. Simple geometric shapes "
            "with bold, even strokes and rounded ends. No gradients, no shadows, no black outlines, "
            "no texture, no text, no letters, no numbers. One centred subject with a wide empty margin."
        )
    return (
        f"A flat, minimal editorial illustration: {spec.prompt}. A restrained palette of teal {a}, "
        f"amber {b} and a warm light grey, on a pure white #FFFFFF background. Clean shapes, no "
        "gradients, no text, no letters, no numbers, no logos. Generous empty margin."
    )


def key_white(path: Path, *, soft: float = 0.18, pad: float = 0.08) -> np.ndarray:
    """RGBA uint8 with white keyed to transparent, trimmed to the ink plus ``pad``."""
    with Image.open(path) as im:
        rgb = np.asarray(im.convert("RGB"), dtype=np.float32) / 255.0
    dist = (1.0 - rgb).max(axis=2)
    alpha = np.clip((dist - 0.03) / soft, 0.0, 1.0)
    safe = np.maximum(alpha, 1e-3)[..., None]
    color = np.clip((rgb - (1.0 - safe)) / safe, 0.0, 1.0)
    ys, xs = np.nonzero(alpha > 0.05)
    if xs.size:
        side = max(xs.max() - xs.min(), ys.max() - ys.min()) + 1
        m = int(side * pad)
        cx, cy = (xs.min() + xs.max()) // 2, (ys.min() + ys.max()) // 2
        half = side // 2 + m
        y0, y1, x0, x1 = cy - half, cy + half, cx - half, cx + half
        out = np.zeros((y1 - y0, x1 - x0, 4), dtype=np.float32)
        sy0, sx0 = max(0, y0), max(0, x0)
        sy1, sx1 = min(rgb.shape[0], y1), min(rgb.shape[1], x1)
        out[sy0 - y0 : sy1 - y0, sx0 - x0 : sx1 - x0, :3] = color[sy0:sy1, sx0:sx1]
        out[sy0 - y0 : sy1 - y0, sx0 - x0 : sx1 - x0, 3] = alpha[sy0:sy1, sx0:sx1]
    else:
        out = np.dstack([color, alpha])
    return np.clip(out * 255 + 0.5, 0, 255).astype(np.uint8)


def _backend(spec: ImageSpec):
    model = spec.model or DEFAULT_MODELS[spec.provider]
    return OpenAIImage(model) if spec.provider == "openai" else GeminiImage(model)


def _request(spec: ImageSpec, theme: str) -> ImageRequest:
    prompt = house_prompt(spec, theme)
    if spec.provider == "openai":
        return ImageRequest(prompt=prompt, width=1024, height=1024, quality=spec.quality)
    return ImageRequest(prompt=prompt, aspect="1:1", size="1K")


async def _generate(video: Video, assets: Path) -> list[dict]:
    cache = GenCache(CACHE)
    rows = []
    for spec in video.images:
        backend = _backend(spec)
        try:
            res = await generate_verified(
                backend, _request(spec, video.theme), cache=cache, rerolls=1, stage=f"image:{spec.id}"
            )
        finally:
            await backend.aclose()
        png = assets / "images" / f"{spec.id}.png"
        png.parent.mkdir(parents=True, exist_ok=True)
        rgba = key_white(res.path)
        Image.fromarray(rgba, "RGBA").save(png)
        to_webp(res.path, png.with_suffix(".webp"), max_width=768)
        receipts = assets / "receipts"
        receipts.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(cache.receipt_path(res.key), receipts / f"image-{spec.id}-{res.key[:12]}.json")
        rows.append(
            {
                "id": spec.id,
                "model": res.receipt.model,
                "cost_usd": res.cost_usd,
                "receipt_cost_usd": res.receipt.cost_usd,
                "cached": res.cached,
                "path": str(png),
            }
        )
    return rows


def generate_images(video: Video, assets: Path) -> list[dict]:
    return asyncio.run(_generate(video, assets)) if video.images else []


def load_images(video: Video, assets: Path) -> dict[str, np.ndarray]:
    out: dict[str, np.ndarray] = {}
    for spec in video.images:
        png = assets / "images" / f"{spec.id}.png"
        if png.is_file():
            with Image.open(png) as im:
                out[spec.id] = np.ascontiguousarray(np.asarray(im.convert("RGBA"), dtype=np.uint8))
    return out
