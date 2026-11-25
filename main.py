"""Frost Epitaph - Famous Last Words: The Funniest Epitaph.

Writes one original one-line epitaph (at most 150 characters) to
/output/entry.txt, or to $MAKEFUN_OUTPUT_DIR/entry.txt when set.
"""
import os

EPITAPH = "Here lies my to-do list. It outlived me, and it still isn't done."


def main():
    text = EPITAPH.strip()
    if not 1 <= len(text) <= 150:
        raise SystemExit(
            f"epitaph is {len(text)} chars, outside the 1-150 gate"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    print(f"wrote {len(text)} chars to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
