#!/usr/bin/env python3
"""Validate the skill, plugin, marketplace and MCP config against the documented
schemas (Agent Skills spec + Claude Code plugin/marketplace reference).

Stdlib only. Exit 0 when everything passes, 1 otherwise.
  python3 scripts/validate.py
"""
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
errors, warnings = [], []

PORTABLE_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
RESERVED_PLUGIN_PREFIXES = ("claude-", "anthropic-", "anthropics-", "cc-plugin-")
RESERVED_PLUGIN_NAMES = {"claude", "anthropic", "claude-code", "claude-mods"}
RESERVED_MARKETPLACES = {
    "claude-plugins-official", "claude-code-plugins", "claude-code-marketplace",
    "anthropic-marketplace", "anthropic-plugins", "agent-skills", "anthropic-agent-skills",
    "knowledge-work-plugins", "claude-community", "claude-plugins-community", "healthcare",
    "npm", "pip", "uv", "cargo", "github", "gh",
}
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def parse_frontmatter(text):
    """Minimal YAML subset: top-level `key: value` and one level of nested map."""
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with '---' frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("frontmatter is not closed with '---'")
    fm, body = text[4:end], text[end + 5:]
    data, current = {}, None
    for i, line in enumerate(fm.splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith((" ", "\t")):
            if current is None or not isinstance(data.get(current), dict):
                raise ValueError(f"frontmatter line {i}: unexpected indentation")
            k, _, v = line.strip().partition(":")
            data[current][k.strip()] = v.strip().strip('"').strip("'")
            continue
        k, sep, v = line.partition(":")
        if not sep:
            raise ValueError(f"frontmatter line {i}: expected 'key: value'")
        k, v = k.strip(), v.strip()
        if k in data:
            raise ValueError(f"frontmatter: duplicate key {k}")
        if v == "":
            data[k] = {}
            current = k
        else:
            data[k] = v.strip('"').strip("'") if v[:1] in "\"'" else v
            current = k
    return data, body


def check_skill(skill_dir):
    p = skill_dir / "SKILL.md"
    rel = p.relative_to(ROOT)
    if not p.exists():
        err(f"{rel}: missing")
        return
    text = p.read_text(encoding="utf-8")
    try:
        fm, body = parse_frontmatter(text)
    except ValueError as e:
        err(f"{rel}: {e}")
        return
    extra = set(fm) - PORTABLE_KEYS
    if extra:
        err(f"{rel}: non-portable frontmatter keys {sorted(extra)} (claude.ai/API reject them)")
    name = fm.get("name", "")
    if not name:
        err(f"{rel}: name is required")
    else:
        if len(name) > 64 or not re.fullmatch(r"[a-z0-9-]+", name) or name.startswith("-") \
                or name.endswith("-") or "--" in name:
            err(f"{rel}: invalid name {name!r} (1-64 chars, a-z 0-9 -, no leading/trailing/double -)")
        if "anthropic" in name or "claude" in name:
            err(f"{rel}: name may not contain 'anthropic' or 'claude'")
        if name != skill_dir.name:
            err(f"{rel}: name {name!r} must equal folder name {skill_dir.name!r}")
    desc = fm.get("description", "")
    if not isinstance(desc, str) or not desc:
        err(f"{rel}: description is required")
    else:
        if len(desc) > 1024:
            err(f"{rel}: description is {len(desc)} chars (max 1024)")
        if re.search(r"<[^>]+>", desc):
            err(f"{rel}: description may not contain XML tags")
        if re.match(r"(?i)^(i|you|we)\b", desc):
            warn(f"{rel}: description should be third person")
        if "use" not in desc.lower():
            warn(f"{rel}: description should say when to use the skill")
    comp = fm.get("compatibility")
    if isinstance(comp, str) and len(comp) > 500:
        err(f"{rel}: compatibility is over 500 chars")
    if "metadata" in fm and not isinstance(fm["metadata"], dict):
        err(f"{rel}: metadata must be a map of strings")
    lines = body.count("\n") + 1
    if lines > 500:
        err(f"{rel}: body is {lines} lines (keep under 500)")
    approx_tokens = len(body) // 4
    if approx_tokens > 5000:
        warn(f"{rel}: body is ~{approx_tokens} tokens (aim for < 5000)")
    # every linked local file must exist; references one level deep
    for target in re.findall(r"\]\(([^)#\s]+)\)", body):
        if target.startswith(("http://", "https://", "mailto:")) or target.startswith("<"):
            continue
        if not (skill_dir / target).exists():
            err(f"{rel}: links to missing file {target}")
        if target.count("/") > 1:
            warn(f"{rel}: {target} is nested more than one level deep")
    for ref in sorted((skill_dir / "references").glob("*.md")) if (skill_dir / "references").exists() else []:
        t = ref.read_text(encoding="utf-8")
        n = t.count("\n") + 1
        if n > 100 and not re.search(r"(?im)^#+\s*(contents|table of contents)", t):
            err(f"{ref.relative_to(ROOT)}: {n} lines without a table of contents")
        if f"references/{ref.name}" not in body:
            warn(f"{ref.relative_to(ROOT)}: not referenced from SKILL.md")
    for script in sorted((skill_dir / "scripts").glob("*")) if (skill_dir / "scripts").exists() else []:
        if script.suffix == ".py":
            src = script.read_text(encoding="utf-8")
            bad = re.findall(r"^\s*(?:import|from)\s+(requests|httpx|aiohttp|bs4|yaml)\b", src, re.M)
            if bad:
                err(f"{script.relative_to(ROOT)}: imports non-stdlib modules {bad}")
    print(f"  skill {name}: {len(desc)}-char description, {lines}-line body, ~{approx_tokens} tokens")


def is_url(u):
    try:
        r = urlparse(u)
        return r.scheme in ("http", "https") and bool(r.netloc)
    except Exception:
        return False


def load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        err(f"{path.relative_to(ROOT)}: missing")
    except json.JSONDecodeError as e:
        err(f"{path.relative_to(ROOT)}: invalid JSON: {e}")
    return None


def check_plugin_name(name, where):
    if not isinstance(name, str) or not KEBAB.match(name):
        err(f"{where}: name {name!r} must be kebab-case")
        return
    if name in RESERVED_PLUGIN_NAMES or name.startswith(RESERVED_PLUGIN_PREFIXES):
        err(f"{where}: name {name!r} is reserved")
    if re.search(r"\bclaude\b", name.replace("-", " ")):
        warn(f"{where}: avoid the word 'claude' in plugin names")


def check_author(a, where):
    if a is None:
        warn(f"{where}: author missing")
        return
    if not isinstance(a, dict) or not a.get("name"):
        err(f"{where}: author must be an object with a name")
    elif a.get("url") and not is_url(a["url"]):
        err(f"{where}: author.url is not a URL")


def check_plugin(plugin_root):
    where = f"{(plugin_root / '.claude-plugin/plugin.json').relative_to(ROOT)}"
    pj = load_json(plugin_root / ".claude-plugin" / "plugin.json")
    if pj is None:
        return None
    check_plugin_name(pj.get("name"), where)
    for k in ("version", "description"):
        if not pj.get(k):
            warn(f"{where}: {k} missing")
    if pj.get("version") and not re.fullmatch(r"\d+\.\d+\.\d+(-[\w.]+)?", pj["version"]):
        warn(f"{where}: version is not semver")
    check_author(pj.get("author"), where)
    for k in ("homepage", "repository"):
        if pj.get(k) and not is_url(pj[k]):
            err(f"{where}: {k} must be a URL")
    if not pj.get("license"):
        err(f"{where}: license missing (directory blocks without it)")
    if "keywords" in pj and not (isinstance(pj["keywords"], list) and all(isinstance(x, str) for x in pj["keywords"])):
        err(f"{where}: keywords must be a list of strings")
    known = {"name", "displayName", "version", "description", "author", "homepage", "repository",
             "license", "keywords", "metadata", "$schema", "icon", "documentationUrl", "supportUrl",
             "privacyPolicyUrl", "termsOfServiceUrl", "defaultEnabled", "dependencies", "userConfig",
             "skills", "commands", "agents", "hooks", "mcpServers", "lspServers", "outputStyles",
             "workflows", "experimental"}
    for k in set(pj) - known:
        warn(f"{where}: unknown field {k}")
    if (plugin_root / ".claude-plugin" / "skills").exists():
        err(f"{where}: skills/ must be at the plugin root, not inside .claude-plugin/")
    if (plugin_root / "bin").exists():
        warn(f"{where}: bin/ makes claude.ai/Cowork refuse the plugin")
    # MCP config
    mcp_path = plugin_root / ".mcp.json"
    if mcp_path.exists():
        mj = load_json(mcp_path)
        if mj is not None:
            servers = mj.get("mcpServers")
            if not isinstance(servers, dict) or not servers:
                err(".mcp.json: needs a non-empty mcpServers object")
            else:
                for sname, cfg in servers.items():
                    t = cfg.get("type")
                    if "url" in cfg:
                        if t not in ("http", "streamable-http", "sse"):
                            err(f".mcp.json {sname}: a url server needs type 'http'")
                        if t == "sse":
                            warn(f".mcp.json {sname}: SSE is deprecated, use http")
                        if not is_url(cfg["url"]):
                            err(f".mcp.json {sname}: url is not a URL")
                    elif "command" not in cfg:
                        err(f".mcp.json {sname}: needs url or command")
    skills_dir = plugin_root / "skills"
    if skills_dir.exists():
        for d in sorted(x for x in skills_dir.iterdir() if x.is_dir()):
            check_skill(d)
    print(f"  plugin {pj.get('name')} {pj.get('version')}")
    return pj


def check_marketplace():
    path = ROOT / ".claude-plugin" / "marketplace.json"
    mj = load_json(path)
    if mj is None:
        return
    where = "marketplace.json"
    name = mj.get("name")
    if not isinstance(name, str) or not KEBAB.match(name):
        err(f"{where}: name must be kebab-case")
    elif name in RESERVED_MARKETPLACES or name.startswith("claudeai-") or \
            (("claude" in name or "anthropic" in name) and "official" in name):
        err(f"{where}: name {name!r} is reserved")
    owner = mj.get("owner")
    if not isinstance(owner, dict) or not owner.get("name"):
        err(f"{where}: owner.name is required")
    if not (mj.get("description") or (mj.get("metadata") or {}).get("description")):
        warn(f"{where}: description missing")
    plugins = mj.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        err(f"{where}: plugins[] is required")
        return
    seen = set()
    for i, p in enumerate(plugins):
        w = f"{where} plugins[{i}]"
        check_plugin_name(p.get("name"), w)
        if p.get("name") in seen:
            err(f"{w}: duplicate plugin name")
        seen.add(p.get("name"))
        src = p.get("source")
        if isinstance(src, str):
            if not src.startswith("./"):
                err(f"{w}: relative source must start with ./")
            root = (ROOT / src).resolve()
            if not root.exists():
                err(f"{w}: source {src} does not exist")
                continue
            pj = check_plugin(root)
            if pj and pj.get("name") != p.get("name"):
                err(f"{w}: name differs from plugin.json name {pj.get('name')!r}")
            if pj and p.get("version") and pj.get("version") != p.get("version"):
                warn(f"{w}: version differs from plugin.json (plugin.json wins)")
        elif isinstance(src, dict):
            if src.get("source") not in ("github", "url", "git-subdir", "npm", "archive", "command"):
                err(f"{w}: unknown source type")
        else:
            err(f"{w}: source is required")
    print(f"  marketplace {name}: {len(plugins)} plugin(s)")


def check_utm():
    for f in [ROOT / "README.md", ROOT / "CONTRIBUTING.md", ROOT / "docs" / "LAUNCH.md"]:
        if not f.exists():
            continue
        for m in re.finditer(r"https?://(?:www\.)?boxerbook\.com[^\s)\"'>`\]]*", f.read_text(encoding="utf-8")):
            u = m.group(0)
            if "/v1/" in u or u.endswith("/mcp") or "mcp.boxerbook.com" in u:
                continue
            if "utm_source=claude-skill" not in u:
                err(f"{f.name}: boxerbook.com link without utm_source=claude-skill: {u}")


def main():
    print("Validating", ROOT)
    check_marketplace()
    check_utm()
    for w in warnings:
        print("  WARN ", w)
    for e in errors:
        print("  ERROR", e)
    print("OK" if not errors else f"FAILED: {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
