"""Funniest autocorrect fail for make.fun (v1).

Writes one autocorrect fail, under 200 characters, to
/output/entry.txt: a client email where "proposal" becomes
"porpoise", and the meeting goes swimmingly. The wrong word is
specific and original, the slip is clear on first read, and the
line reads as a real message that went wrong. One line, 138
characters.
"""

import os

TEXT = (
    "I told the client 'Please find the attached proposal' \u2014 "
    "autocorrect sent 'Please find the attached porpoise.' "
    "The meeting went swimmingly."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 199, "entry must be 1-199 characters, got %d" % len(TEXT)
    assert "\n" not in TEXT, "entry must be a single line"
    assert TEXT == TEXT.strip(), "entry must not start or end with whitespace"
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
