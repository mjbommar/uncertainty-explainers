# Structure: the red thread

Review of the first build (2026-09-23): every vignette works alone and nothing
connects them. Video 2 changes subject five times without a bridge sentence.
Video 3 is a chain of "here is another case". A viewer cannot say what the
video is arguing or where it is going. This document fixes the shape. It
binds every script. `docs/SCRIPT-BRIEF.md` still governs voice and visuals.

## The shape of every video

1. **Pose the problem** (20 to 40 s). One concrete scene, then one question
   the viewer wants answered. No definitions yet. The question is the thread.
2. **State the claim and show the map** (15 to 30 s). One sentence of thesis.
   Then the `roadmap` scene: the stops we will visit, each named as a short
   question, in order. The narration reads the stops.
3. **The stops** (the body). Each stop has three parts:
   - **Bridge in** (one or two sentences, over the `roadmap` scene with the
     next stop lighting up): what the last stop settled, and why that raises
     this stop's question. The bridge names the previous takeaway in words.
   - **The vignette** (the existing material, cut to what serves the question).
   - **Takeaway** (one sentence, on screen as a line of text as well as
     spoken): the stop's answer, written so it can be read back in the ending.
4. **Zoom out** (40 to 70 s). The `roadmap` with every stop lit and every
   takeaway shown. Narration reads the takeaways as one chain of reasoning,
   in order, with "so" and "but" between them, not as a list. Then return to
   the opening scene and answer its question with the chain. Then one
   sentence of hand-off to the next video.

Rules that follow:

- The opening question is asked in words at the start and answered in words
  at the end. Same words.
- No stop starts without a bridge that names what came before.
- No stop ends without a takeaway. The takeaways are the spine; write them
  first, then the bridges, then cut the vignettes to fit.
- Cut material that does not serve a takeaway, however good the visual.
- Segment count is not the target. Stops are. A stop is 40 to 120 s.
- The `roadmap` scene returns at every bridge, for 3 to 6 s, so the viewer
  always knows where they are. It is the connective tissue on screen; the
  bridge sentence is the connective tissue in the ear.

## The `roadmap` scene (shared, in `pipeline/scenes_shared.py`)

Params: `stops` (list of `{label, question, takeaway?}`), `current`
(index, or -1 for the overview, or `len(stops)` for the zoom-out), `mode`
(`overview` | `travel` | `summary`). Draws a horizontal path with one node
per stop: label under the node, question above the current node, takeaway
under each completed node in `summary` mode. Completed nodes are teal, the
current node amber and pulsing, future nodes dim. The path fills to the
current node. Ambient: a slow drift of the fill. Must fit 4 to 6 stops with
labels of up to 3 words and takeaways of up to 9 words on a 1920 stage.

---

## Video 1: Two kinds of not knowing (2.5 to 3.5 min)

**Opening scene and question.** Three people each say "I do not know." One
holds a die about to be rolled. One holds a sealed envelope with a number
inside. One is asked the price of copper twenty years from now. Same three
words. *Question: when someone says they do not know, what exactly is it
they do not know, and does the difference matter?*

**Claim.** Uncertainty is not one thing. Two questions sort it: is the gap
chance or ignorance, and can it be measured? The answers decide what any
number about it can mean.

**Map.** Stop 1, Chance or ignorance? Stop 2, Can it be measured? Stop 3,
What if the odds themselves are unknown? Stop 4, Where does mine sit?

| Stop | Vignette (cut from current script) | Takeaway |
|---|---|---|
| 1. Chance or ignorance? | Die and envelope; aleatory and epistemic; "the job of the model builder" [S01] | Chance stays. Ignorance can be closed with data. |
| 2. Can it be measured? | Knight's fire insurance and the new venture [S76, S02]; Keynes's roulette, copper, "we simply do not know" [S04] | A number needs a group of similar cases. Without one, there is no number. |
| 3. What if the odds are unknown? | Ellsberg's two urns [S77, S23] | Between the two: outcomes known, odds not. People treat that differently, and so should a forecast. |
| 4. Where does mine sit? | The scale from certainty to total ignorance [S08, S09] | Every forecast should first say where on the scale it stands. |

**Bridges.**
- Into 1: "Start with the die and the envelope. They fail for different reasons."
- Into 2: "So ignorance can shrink and chance cannot. But a second question hides inside the first. Even chance only gets a number when we can count something."
- Into 3: "Knight and Keynes drew a hard line: measurable or not. Most real cases sit between, and Ellsberg showed how people behave there."
- Into 4: "Chance, ignorance, no group to count, unknown odds. These are not four boxes. They are stops on one scale."

**Zoom out.** Roadmap in summary mode. Chain: "Chance stays and ignorance can be closed, so the first job is to say which. But a number needs a group of cases, so the second job is to say whether one exists. Where the odds themselves are unknown, a single number claims too much. So every forecast should say where on the scale it stands." Return to the three people: the die is chance with a number; the envelope is ignorance with a number waiting; the copper price is on the far end, and no honest number exists. Hand-off: "Once you know which kind you face, the next question is what a number can honestly say. That is the next video."

---

## Video 2: From evidence to forecast (6 to 7 min)

**Opening scene and question.** A test comes back positive. Ninety-five of a
hundred physicians, asked what that means, say seventy to eighty percent. The
right answer is under eight [S59]. Same test, same evidence, one number ten
times too big. *Question: where does a probability come from, and how can you
tell whether it is any good?*

**Claim.** A probability is a summary of evidence, not a fact about the
world. So it can be built well or badly, it can claim more than the evidence
holds, and it can be checked.

**Map.** Stop 1, What is the number counting? Stop 2, How should evidence move
it? Stop 3, When is one number too many? Stop 4, What can it say about the
future? Stop 5, How do we know it was good?

| Stop | Vignette | Takeaway |
|---|---|---|
| 1. What is it counting? | Three meanings [S15]; the reference class (man, non-smoker, professor) [S15]; Laplace's sunrise and the astronomer [S16]; the cube (keep short or cut) | A probability counts over a group. Name the group or the number floats. |
| 2. How should evidence move it? | Bayes; the 1,000 women [S59, S21]; why physicians got it wrong; counts beat percentages. This stop resolves the opening. | Start from how common it is, then let the test move you. Rare things stay rare after one test. |
| 3. When is one number too many? | The coin tossed 100 times versus the coin never seen; Ellsberg's interval [S23]; Betty and Dempster-Shafer [S24] | When evidence is thin, an honest summary is a range, not a point. |
| 4. What can it say about the future? | Hume [S28]; Lorenz and the ensemble [S44, S45]; forecast, projection, scenario, counterfactual [S46, S38, S39, S42]; Pearl's rungs [S39] | A forecast leans on the past and on a model. Say which kind of claim it is, and show the spread. |
| 5. How do we know it was good? | Brier [S34]; calibration; overconfidence [S32]; Good Judgment [S34] | One outcome proves nothing. Many forecasts, scored, do. |

**Bridges.**
- Into 1: "To see where the doctors went wrong, start with what a probability is counting."
- Into 2: "So the group matters. The doctors had the right group and still missed by a factor of ten. The error was in how they let the test move the number."
- Into 3: "Bayes gives one number, and for the test that was enough. But sometimes one number claims more than the evidence holds."
- Into 4: "A range is honest about today's evidence. Forecasts reach further: they claim something about a future no one has seen."
- Into 5: "So a forecast is a claim built from evidence and a model. A claim can be graded. That is the last stop."

**Zoom out.** Chain: "A probability counts over a group, so name the group. Evidence moves it by Bayes' rule, so start from the base rate. Thin evidence earns a range, not a point. A forecast adds a model and a kind of claim, so say which and show the spread. And none of this is trusted until it is scored." Return to the test: 7.8 percent is a count over a thousand women like this one, moved by one test, stated as a point because the evidence is good, and checkable. Hand-off: "A scored number can still fail. It fails when the listener hears a different number than the one you meant. That is the next video."

---

## Video 3: Saying it out loud (9 to 10 min)

**Opening scene and question.** Bay of Pigs, 1961. "A fair chance." The
writer meant about three in ten. The readers heard yes [S68, S67, S69].
*Question: where, between the writer and the reader, did seven in ten
disappear, and how do you stop it happening?*

**Claim.** Uncertainty is not communicated until the listener holds the number
the speaker meant. A message about uncertainty has parts that can each fail:
the word, the number, the group it counts over, the picture. And it needs one
more part that is usually missing: how good the evidence is.

**Map.** Stop 1, The word. Stop 2, The number's group. Stop 3, The picture.
Stop 4, The single result. Stop 5, When institutions refuse numbers. Stop 6,
The whole statement.

| Stop | Vignette | Takeaway |
|---|---|---|
| 1. The word | Kent's "serious possibility" and his Board [S47]; ICD 203 and IPCC ladders, "likely" twice [S50, S51]; pull to the middle [S53]; the bracket fix [S55] | A word carries a number only if the number is beside it. |
| 2. The number's group | "30 percent chance of rain", five cities [S60, S65] | A number needs its reference class, or the listener supplies their own. |
| 3. The picture | The cone and Charley [S64, S63]; "skinny black line" | A picture of uncertainty is read as a picture of certainty unless it says what it leaves out. |
| 4. The single result | 2016, 71 against 29 [S61, S62] | One outcome cannot judge a probability. Say so before the outcome arrives. |
| 5. When institutions refuse numbers | ASC 450 words, the tax exception [S71, S73]; Addington's three standards [S75] | Some ladders are words on purpose, tied to actions. Know which ladder you are on. |
| 6. The whole statement | van der Bles [S56, S57]; confidence versus likelihood [S50]; the sentence builder | Say the word, the number, the group, and how good the evidence is. |

**Bridges.**
- Into 1: "Start with the word itself. Kent found the fault ten years before the Bay of Pigs."
- Into 2: "A number beside the word fixes the word. But a number can fail too, when the listener does not know what it counts over."
- Into 3: "Words and numbers fail in the ear. Pictures fail in the eye, and the largest case is a hurricane."
- Into 4: "Suppose the word, the number, the group and the picture are all right. The listener still judges the forecast by one outcome."
- Into 5: "If words fail so often, why not always use numbers? Some institutions refuse them on purpose, and it is worth seeing why."
- Into 6: "So: a word, a number, a group, a picture, and a warning about single results. Van der Bles and colleagues put the pieces into one statement, and added the one that is usually missing."

**Zoom out.** Chain: "A word needs a number beside it. A number needs its group. A picture needs to say what it leaves out. No single outcome can judge it. Some ladders are words on purpose. And the whole thing needs a statement of how good the evidence is." Return to the memo and rewrite it in full form: "The plan has a fair chance: about three in ten, judged against operations of this kind, and our confidence in that number is low." Then the drafting officer, fifteen years later, who had not insisted on the number [S67]. End line: "Say the word. Then say the number."
