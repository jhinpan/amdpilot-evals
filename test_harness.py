from pathlib import Path

repo = Path(__file__).resolve().parent
committed = (repo / "delivery_e2e_probe" / "committed.txt").read_text()
uncommitted = (repo / "delivery_e2e_probe" / "uncommitted.txt").read_text()
assert committed == "committed-change\n", committed
assert uncommitted == "runtime-clean\n", uncommitted
print("SCORE: 123.0")
