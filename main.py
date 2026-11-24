#!/usr/bin/env python3
"""Two Lines to Your Past Self (make.fun) -- writes two lines to /output/entry.txt.

The entry, exactly two lines and two sentences:

  Line 1 warns the past self about ONE specific moment: deleting a
  voicemail -- named by who left it (grandmother), when (your birthday
  in 2019), and the exact words in it (she sings off-key and calls
  you her brave boy). A time, a person, and a sentence said out loud:
  concrete enough to picture, not a vague phase of life.

  Line 2 traces the cause and effect instead of restating the
  warning: replaying it after her funeral, and it being the only
  recording of her voice you will ever have. The loss is irreversible
  precisely because the moment in line 1 was the last copy.

The voice is plain and addressed to one person, with no wasted words
and no cleverness for its own sake. The twist is the reversal in
line 2: the throwaway message becomes the only thing left.
"""
import os

LINE_1 = "Don't delete the voicemail your grandmother left on your birthday in 2019, singing off-key and calling you her brave boy."
LINE_2 = "You will replay it a hundred times after her funeral, and it is the only recording of her voice you will ever have."

TEXT = LINE_1 + "\n" + LINE_2


def main() -> None:
    # Self-check the same gate the sealed scorer applies: UTF-8 text of
    # 1 to 280 characters, not only white space. Fail loudly here rather
    # than silently writing an invalid entry.
    if not (1 <= len(TEXT) <= 280 and TEXT.strip()):
        raise SystemExit(f"entry is {len(TEXT)} chars, gate needs 1-280")
    lines = TEXT.split("\n")
    if len(lines) != 2:
        raise SystemExit(f"entry must be exactly 2 lines, got {len(lines)}")
    for i, line in enumerate(lines, 1):
        if line.count(".") != 1 or not line.endswith("."):
            raise SystemExit(f"line {i} must be exactly one sentence: {line!r}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the file is exactly the two lines, nothing else.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
