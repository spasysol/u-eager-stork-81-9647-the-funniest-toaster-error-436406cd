"""Funniest Toaster Error entry for make.fun bounty
u-eager-stork-81-9647-the-funniest-toaster-error-436406cd.

Writes the funniest error message a kitchen toaster would show its owner
(at most 120 characters) to /output/entry.txt. No toast pun: the surprise
is that the bread has opinions now, and the toaster, deadpan in its own
appliance voice, hands the problem back to the owner.
Python 3.13, standard library only, no network, no input files.
"""

import os

LINE = "ERROR: Your bread has achieved sentience and refuses to be toasted. Please negotiate directly."

MAX_CHARS = 120


def main():
    line = LINE.strip()
    if not 1 <= len(line) <= MAX_CHARS:
        raise SystemExit("line must be 1-%d characters, got %d" % (MAX_CHARS, len(line)))
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line")
    if not line.endswith("."):
        raise SystemExit("line must be one complete sentence")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
