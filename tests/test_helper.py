"""Live tests of skills/boxing/scripts/boxerbook.py against the public Boxerbook API.

  python3 -m unittest discover -s tests -v
Needs network access to boxerbook.com. Assertions are about shape and stable
facts (ids, slugs, historical bouts), not about values that change weekly.
"""
import json
import subprocess
import sys
import unittest
from pathlib import Path

HELPER = Path(__file__).resolve().parent.parent / "helper" / "boxerbook.py"


def run(*args):
    p = subprocess.run([sys.executable, str(HELPER), *args], capture_output=True, text=True, timeout=120)
    return p.returncode, (json.loads(p.stdout) if p.stdout.strip() else None), p.stderr


class HelperLive(unittest.TestCase):
    def test_search(self):
        code, d, _ = run("search", "canelo")
        self.assertEqual(code, 0)
        self.assertTrue(any(r["slug"].startswith("canelo-alvarez") for r in d["results"]))
        self.assertIn("utm_source=claude-skill", d["results"][0]["url"])

    def test_boxer_by_name_and_slug(self):
        code, d, _ = run("boxer", "Oleksandr Usyk")
        self.assertEqual(code, 0)
        self.assertEqual(d["slug"], "oleksandr-usyk-q938027")
        for k in ("record", "stance", "height_cm", "reach_cm", "last_result", "url", "attribution"):
            self.assertIn(k, d)
        code, d2, _ = run("boxer", "oleksandr-usyk-q938027")
        self.assertEqual(d2["id"], d["id"])

    def test_bouts_history(self):
        code, d, _ = run("bouts", "canelo", "--limit", "3")
        self.assertEqual(code, 0)
        self.assertEqual(len(d["bouts"]), 3)
        self.assertGreater(d["total"], 60)
        dates = [b["date"] for b in d["bouts"]]
        self.assertEqual(dates, sorted(dates, reverse=True))

    def test_h2h_met_and_never_met(self):
        code, d, _ = run("h2h", "Usyk", "Dubois")
        self.assertTrue(d["met"])
        self.assertIn("2023-08-26", [m["date"] for m in d["meetings"]])
        code, d, _ = run("h2h", "Tyson Fury", "Canelo")
        self.assertFalse(d["met"])
        self.assertIn("no bout on record", d["note"])

    def test_bout(self):
        code, d, _ = run("bout", "25025")  # Crawford vs Canelo, 13 Sep 2025
        self.assertEqual(code, 0)
        self.assertEqual(d["date"], "2025-09-13")
        self.assertEqual(d["method"], "UD")
        self.assertNotIn("signals", d)
        code, full, _ = run("--full", "bout", "25025")
        self.assertIsInstance(full["sources"][0], dict)

    def test_next(self):
        code, d, _ = run("next", "Usyk")
        self.assertEqual(code, 0)
        self.assertIn("next_fight", d)

    def test_schedule(self):
        code, d, _ = run("schedule", "--when", "30d")
        self.assertEqual(code, 0)
        self.assertIn("events", d)
        for e in d["events"][:5]:
            self.assertIn("bouts", e)
            self.assertIn("broadcasts", e)

    def test_results(self):
        code, d, _ = run("results", "--days", "14")
        self.assertEqual(code, 0)
        self.assertIn("bouts", d)
        if d["bouts"]:
            self.assertIn(d["bouts"][0]["winner"], ("a", "b", "draw", "nc"))

    def test_rankings(self):
        for pub in ("boxerbook", "wbc", "ring"):
            code, d, _ = run("rankings", "hea", "--publisher", pub)
            self.assertEqual(code, 0, pub)
            self.assertEqual(d["publisher"], pub)
            self.assertGreaterEqual(len(d["items"]), 5)
        code, d, _ = run("rankings", "w_fly")
        self.assertEqual(d["division"]["code"], "w_fly")

    def test_status(self):
        code, d, _ = run("status")
        self.assertGreater(d["boxers"], 10000)

    def test_errors(self):
        code, d, err = run("boxer", "Zzyzx Qwertyuiop")
        self.assertEqual(code, 1)
        self.assertIn("no boxer matches", err)
        code, d, err = run("rankings", "nope")
        self.assertEqual(code, 1)
        self.assertIn("404", err)


if __name__ == "__main__":
    unittest.main()
