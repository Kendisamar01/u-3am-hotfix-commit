import os
import subprocess
import sys
from pathlib import Path

output_dir = "/tmp/hotfixout"
entry_path = Path(output_dir) / "entry.txt"
env = dict(os.environ)
env["MAKEFUN_OUTPUT_DIR"] = output_dir
entry_path.unlink(missing_ok=True)
subprocess.run(
    [sys.executable, "main.py"],
    cwd=Path(__file__).resolve().parent,
    env=env,
    check=True,
)
text = entry_path.read_bytes().decode("utf-8")
assert len(text.splitlines()) == 1
assert text == text.strip()
assert 1 <= len(text) <= 179
print("PASS")
