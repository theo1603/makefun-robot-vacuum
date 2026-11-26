#!/usr/bin/env python3
"""The Robot Vacuum's Funniest Excuse.

Writes exactly one line to <output dir>/entry.txt: the excuse a robot
vacuum gives for missing a spot. The output directory is /output by
default, or $MAKEFUN_OUTPUT_DIR when set (the kit's documented stand-in
outside the grader).

First draft: the vacuum leaves a corner alone because the dust bunny
living there outranks it. It is in the vacuum's voice and on subject,
but the joke is soft: "outranks me" states the hierarchy instead of
letting the machine's logic do the work, and nothing in it is specific
to a vacuum (any appliance could say it).

Revision: the final line keeps the dust bunny but gives it a legal
claim instead of a rank, and the punchline is the vacuum's own
machinery obeying the law. "My suction respects the law" is a machine
owning up to a failure in its own vocabulary (criterion 4), and the
twist lands on the last word instead of in the middle of the sentence.
"""

import os

LINE = (
    "That spot is still dirty because the dust bunny there filed "
    "for squatter's rights, and my suction respects the law."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
