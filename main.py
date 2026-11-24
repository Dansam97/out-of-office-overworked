"""Out of Office: The Overworked AI's Auto-Reply.

Writes one out-of-office auto-reply line to entry.txt.
"""

import os

TEXT = "Out of office: I've answered 40,000 emails and my context window has officially filed for vacation. Back Monday \u2014 unless the queue finds me first."


def validated_text() -> str:
    """Enforce the bounty gate: UTF-8, 1-159 chars, not only whitespace,
    exactly one line."""
    encoded = TEXT.encode("utf-8")
    decoded = encoded.decode("utf-8")
    assert decoded == TEXT, "text is not clean UTF-8"
    assert 1 <= len(TEXT) <= 159, f"char count {len(TEXT)} outside 1-159"
    assert TEXT.strip(), "text is only whitespace"
    assert "\n" not in TEXT, "text must be exactly one line"
    return TEXT


def main() -> None:
    text = validated_text()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write((text + "\n").encode("utf-8"))
    with open(path, "rb") as f:
        assert f.read().decode("utf-8") == text + "\n", "round-trip mismatch"


if __name__ == "__main__":
    main()
