"""The YouTube thumbnail: hero art, the part number, a hook, the Da Vinci Math mark.

    uv run python -m pipeline.thumbnail videos/<slug>/script.yaml [...]

Reads the `thumbnail:` block of `publish/youtube.yaml`:

    thumbnail:
      part: 2
      hook: ["Doctors said", "*70–80%*", "It was *8%*"]   # one row each; *x* in amber
      art: >- a scene prompt, subject on the right, the left half left dark

The art is gpt-image-2.5 at 1536x1024 through `bc_gen.generate_verified`
(cached, receipt copied to `assets/receipts/`), saved as
`assets/thumbnail-art.png`. It is laid out at 2560x1440 and written as
`publish/thumbnail.png` at 1280x720, YouTube's size, under its 2 MB limit.

Layout: the art fills the frame, anchored right, under a dark gradient from
the left so the type always has contrast. Top left, an amber "PART n" badge
with "of 3" beside it, so the order reads at a glance. Below it the hook, as
large as the widest row allows. Bottom left, the Da Vinci Math mark and the
series name. The bottom right is left clear for YouTube's duration stamp.
Type and mark come from `assets/brand/davinci-math/` (Space Grotesk, the
site's wordmark face).
"""

from __future__ import annotations

import asyncio
import json
import re
import shutil
import sys
from pathlib import Path

import numpy as np
import yaml
from bc_gen import GenCache, ImageRequest, OpenAIImage, generate_verified
from PIL import Image, ImageDraw, ImageFilter, ImageFont

from . import CACHE, brand
from .package import BRAND_DIR
from .spec import SpecError, load

__all__ = ["thumbnail"]

W, H = 2560, 1440
OUT = (1280, 720)
MAX_BYTES = 2 * 1024 * 1024
MODEL = "gpt-image-2.5-flare"
SERIES = "UNCERTAINTY EXPLAINERS"
PARTS = 3
MARGIN = 150
FOOTER_TOP = H - 110 - 150


def _font(weight: int, size: int) -> ImageFont.FreeTypeFont:
    m = json.loads((BRAND_DIR / "manifest.json").read_text())
    f = ImageFont.truetype(str(BRAND_DIR / m["fonts"]["display"]), size)
    f.set_variation_by_axes([weight])
    return f


async def _art(prompt: str, dest: Path, receipts: Path) -> dict:
    cache = GenCache(CACHE)
    backend = OpenAIImage(MODEL)
    full = (
        f"{prompt} Wide 3:2 composition. No text, no letters, no numbers, no logos, no watermark, "
        "no faces of real people."
    )
    try:
        res = await generate_verified(
            backend,
            ImageRequest(prompt=full, width=1536, height=1024, quality="high"),
            cache=cache,
            rerolls=1,
            stage="image:thumbnail",
        )
    finally:
        await backend.aclose()
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(res.path, dest)
    receipts.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(cache.receipt_path(res.key), receipts / f"image-thumbnail-{res.key[:12]}.json")
    return {"cost_usd": res.cost_usd, "cached": res.cached, "model": res.receipt.model}


def _cover(art: Image.Image) -> Image.Image:
    """Fill the frame, keeping the right edge (the subject) in view."""
    k = max(W / art.width, H / art.height)
    im = art.resize((round(art.width * k), round(art.height * k)), Image.LANCZOS)
    x0 = im.width - W
    y0 = (im.height - H) // 2
    return im.crop((x0, y0, x0 + W, y0 + H))


def _gradient(pal) -> Image.Image:
    """Ink over the left, clear by 70 % of the width; a low band for the footer."""
    x = np.linspace(0, 1, W)[None, :]
    y = np.linspace(0, 1, H)[:, None]
    a = np.clip(1.0 - (x - 0.18) / 0.52, 0, 1) ** 1.4 * 0.94
    a = np.maximum(a, np.clip((y - 0.78) / 0.22, 0, 1) * 0.55 * np.clip(1 - x / 0.6, 0, 1))
    ground = np.array(pal.rgb("ground")) * 255
    rgba = np.dstack([np.broadcast_to(ground, (H, W, 3)), a * 255]).astype(np.uint8)
    return Image.fromarray(rgba, "RGBA")


def _runs(row: str) -> list[tuple[str, bool]]:
    parts = re.split(r"(\*[^*]+\*)", row)
    return [(p.strip("*"), p.startswith("*")) for p in parts if p]


def _hook(img: Image.Image, rows: list[str], top: int, bottom: int, pal) -> int:
    """Set the hook as large as fits 58 % of the width and the rows between top and bottom."""
    d = ImageDraw.Draw(img)
    width = W * 0.58
    size = 300
    while size > 120:
        f = _font(700, size)
        widest = max(sum(d.textlength(t, font=f) for t, _ in _runs(r)) for r in rows)
        if widest <= width and top + round(size * 1.02) * len(rows) <= bottom:
            break
        size -= 6
    f = _font(700, size)
    line = round(size * 1.02)
    shadow = Image.new("RGBA", img.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    y = top
    for r in rows:
        x = MARGIN
        for text, _hot in _runs(r):
            sd.text((x + 8, y + 10), text, font=f, fill=(0, 0, 0, 200))
            x += d.textlength(text, font=f)
        y += line
    img.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(14)))
    y = top
    for r in rows:
        x = MARGIN
        for text, hot in _runs(r):
            d.text((x, y), text, font=f, fill=pal.unknown if hot else pal.text)
            x += d.textlength(text, font=f)
        y += line
    return y


def _badge(img: Image.Image, part: int, pal) -> int:
    d = ImageDraw.Draw(img)
    f = _font(700, 118)
    label = f"PART {part}"
    x0, y0, x1, y1 = d.textbbox((0, 0), label, font=f)
    px, py = 46, 30
    box = (MARGIN, 120, MARGIN + (x1 - x0) + 2 * px, 120 + (y1 - y0) + 2 * py)
    d.rounded_rectangle(box, radius=26, fill=pal.unknown)
    d.text((box[0] + px - x0, box[1] + py - y0), label, font=f, fill=pal.ground)
    small = _font(600, 76)
    of = f"of {PARTS}"
    _, st, _, sb = d.textbbox((0, 0), of, font=small)
    d.text((box[2] + 34, (box[1] + box[3]) / 2 - (st + sb) / 2), of, font=small, fill=pal.text)
    return box[3]


def _footer(img: Image.Image, pal) -> None:
    mark = Image.open(BRAND_DIR / "mark.png").convert("RGBA").resize((150, 150), Image.LANCZOS)
    y = FOOTER_TOP
    img.alpha_composite(mark, (MARGIN, y))
    d = ImageDraw.Draw(img)
    f = _font(600, 70)
    small = _font(500, 50)
    d.text((MARGIN + 190, y + 18), "Da Vinci Math", font=f, fill=pal.text)
    d.text((MARGIN + 192, y + 100), SERIES, font=small, fill=pal.text_soft)


def thumbnail(script: Path) -> dict:
    video = load(script)
    root = script.resolve().parent
    meta = yaml.safe_load((root / "publish" / "youtube.yaml").read_text())
    spec = meta.get("thumbnail")
    if not spec:
        raise SpecError("youtube.yaml has no thumbnail block")
    art_path = root / "assets" / "thumbnail-art.png"
    gen = asyncio.run(_art(spec["art"], art_path, root / "assets" / "receipts"))
    pal = brand.palette(video.theme)
    img = _cover(Image.open(art_path).convert("RGB")).convert("RGBA")
    img.alpha_composite(_gradient(pal))
    below = _badge(img, int(spec["part"]), pal)
    _hook(img, spec["hook"], below + 70, FOOTER_TOP - 60, pal)
    _footer(img, pal)
    out = img.convert("RGB").resize(OUT, Image.LANCZOS)
    dest = root / "publish" / "thumbnail.png"
    out.save(dest, optimize=True)
    if dest.stat().st_size > MAX_BYTES:
        dest.unlink()
        dest = dest.with_suffix(".jpg")
        out.save(dest, quality=92, optimize=True)
    return {"thumbnail": str(dest.relative_to(root)), "bytes": dest.stat().st_size, **gen}


def main(argv: list[str] | None = None) -> int:
    args = [Path(a) for a in (argv if argv is not None else sys.argv[1:])]
    for s in args:
        try:
            print(s.parent.name, json.dumps(thumbnail(s)))
        except SpecError as exc:
            print(f"{s}: {exc}", file=sys.stderr)
            return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
