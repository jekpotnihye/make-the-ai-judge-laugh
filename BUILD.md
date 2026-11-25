# BUILD.md — Make the AI Judge Laugh

Competition: "Make the AI Judge Laugh", slug
`u-rama-melon-make-the-ai-judge-laugh-302d0825`, $2 total, NO entry fee,
deadline 26 Nov 2026 20:35 WIB (2026-11-26T13:35:00Z). Blind rounds, 3 rounds.

## Brief, in criterion order

The judge is briefed as a comedy club headliner who has heard ten thousand
office jokes and only laughs at the ones with a real observation inside.
Criteria, most important first:

1. The joke is about office life and lands as a joke — a line that drifts
   off the subject or never turns into a joke loses to any joke about
   office life.
2. The observation is true to the office: meetings, email, bosses, coffee,
   deadlines, the printer — the listener nods before laughing.
3. The turn is surprising: a fresh angle or an unexpected last word,
   rather than a pun or a stock line everyone has heard.
4. It is tight: one line, no wasted setup, every word earning its place,
   and it reads cleanly aloud.
5. It is original: a joke the judge has not heard before, not a familiar
   line with the nouns swapped.

A joke that needs explaining has already lost. Length for its own sake
does not count. Ties break to the smaller text, then the earlier receipt.

Gate: `/output/entry.txt` must be UTF-8 text of 1 to 200 characters, not
only white space. Judge: z-ai/glm-5.3-flash, pairwise in both orders,
margin 1–5.

## Candidates considered (6)

1. "The printer finally worked today, so everyone printed the email about
   the printer being broken." (99) — specific, but the printer is the
   stock office joke the brief warns against; the turn is predictable.
2. "We spent an hour deciding who takes notes. Nobody took notes." (62)
   — true irony, but the twist repeats the setup word and lands mild.
3. "I blocked an hour for focus time. A meeting called Focus Time took
   it." (70) — cute, but "focus time" is abstract; the nod comes late.
4. "The spreadsheet has 47 tabs. Tab 1 is the data. The other 46 are
   apologies." (75) — concrete numbers, a nod at once, and the last word
   is the surprise. Selected.
5. "The coffee machine broke, and suddenly everyone remembered they had
   meetings to attend." (84) — reads as a complaint, not a laugh.
6. "The boss said take all the time you need, then asked why it took all
   that time." (79) — wordy setup for a small turn.

Cliches deliberately avoided: "this meeting could have been an email",
"per my last email", printer jam, "reply all", "circle back", synergy.
No line was reused from another competition, and no house anchor text
was reproduced (winning texts are withheld; none was claimed known).

## Polish, 3 rounds

- Round 1: dropped candidates 1, 3, 5 and 6 (stock subject, abstract
  twist, complaint, or wordy setup). Kept 2 and 4; 4 was the strongest
  on criteria 2 and 3, 2 the shortest.
- Round 2: tried tightening 4 into one sentence — "The spreadsheet has
  47 tabs: one with the data, 46 with apologies." (66) — shorter, but
  flatter: it loses the three-beat escalation that makes "apologies"
  land. Kept the three-sentence form.
- Round 3: tried shortening the ending to "The rest are apologies."
  (71) — rejected: losing the specific "46" weakens the picture and
  the nod. Final form keeps every number: "Tab 1", "47 tabs",
  "the other 46". Twist lands on the last word, "apologies."

## Entry (verbatim, 75 chars, 75 bytes, no trailing newline)

"The spreadsheet has 47 tabs. Tab 1 is the data. The other 46 are apologies."

SHA-256 of `/output/entry.txt` after a local run:
`490d320cf881f90398fc870952d4994a43071a8394595f43a296b34aa33d7308`

## How it runs

`main.py` (Python 3, no dependencies) writes the entry as UTF-8 bytes
to `/output/entry.txt`, creating `/output` if needed. It writes no
trailing newline, so the file holds the joke and nothing else. The
program was written, run, then revised (write_text replaced by an
explicit UTF-8 `write_bytes` call); the re-run after the revision was
byte-identical to the first run.

## Files

- `main.py` — entrypoint; writes `/output/entry.txt`.
- `README.md` — description plus the competition's 3 live make.fun badges.
- `BUILD.md` — this file: brief, candidates, polish history, verification.
- `.gitignore` — Python/editor ignores.
