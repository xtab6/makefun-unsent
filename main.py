"""Write one two-part micro-confession to $MAKEFUN_OUTPUT_DIR/entry.txt.

The entry is a fixed, deterministic text: a To: line naming who the
unsent message was meant for, and the message itself, one line written
exactly as it was typed. No clock, no randomness, no network, no input.
Only the contents of the output directory are cleaned, never the
directory itself (the grader mounts it).
"""

import os

ENTRY = (
    "To: Dad, who still tells everyone I left the family shop "
    "for a better job\n"
    "i didn't leave for a better job. i left because i couldn't keep "
    "watching you give your whole life to that counter and get "
    "nothing back"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    # Clean only the contents of the output directory, never the dir.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    text = ENTRY
    assert 1 <= len(text) <= 260, len(text)
    assert text.strip(), "entry must not be only whitespace"
    lines = text.split("\n")
    assert len(lines) == 2, "entry must be exactly two parts"
    assert lines[0].startswith("To: "), "first part must be the To: line"
    assert "\n" not in lines[1], "message must be one line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
