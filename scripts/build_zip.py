#!/usr/bin/env python3
"""Build dist/boxing-skill.zip for claude.ai upload (Settings > Capabilities > Skills)
and the Skills API. The zip root is the skill folder: boxing/SKILL.md.

  python3 scripts/build_zip.py
"""
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "boxing"
DIST = ROOT / "dist"
SKIP = {"__pycache__", ".DS_Store"}


def main():
    DIST.mkdir(exist_ok=True)
    out = DIST / "boxing-skill.zip"
    files = sorted(p for p in SKILL.rglob("*") if p.is_file() and not (set(p.parts) & SKIP) and p.suffix != ".pyc")
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for p in files:
            info = zipfile.ZipInfo(str(Path("boxing") / p.relative_to(SKILL)), date_time=(2026, 1, 1, 0, 0, 0))
            info.external_attr = (0o755 if p.suffix == ".py" else 0o644) << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, p.read_bytes())
    size = sum(p.stat().st_size for p in files)
    print(f"{out.relative_to(ROOT)}: {len(files)} files, {size/1024:.1f} KiB uncompressed, {out.stat().st_size/1024:.1f} KiB zipped")
    for p in files:
        print("  boxing/" + str(p.relative_to(SKILL)))


if __name__ == "__main__":
    main()
