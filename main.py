LINE = "When my grandmother finally beat the video game, she stood up, raised the controller over her head, and my whole family cheered like she had just won the World Cup."

# The entry must be one or two lines of 1-280 characters.
assert 1 <= len(LINE) <= 280, f"line is {len(LINE)} chars"
assert LINE == LINE.strip(), "line must not have leading or trailing whitespace"

import os

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)

with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)

# Read back and verify: a silent bad write must fail loudly, not ship a wrong entry.
with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
    assert f.read() == LINE, "entry.txt does not match LINE after write"
