"""Rebuild README.md from the Unraid templates (*.xml) in the repository root.

Each template adds a row with its name, project link, description (first sentence of its
<Overview>) and the command that installs it. Run from the repository root.
"""
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
RAW = "https://raw.githubusercontent.com/dodert/unraid-templates/main"


def text(root, tag):
    return (root.findtext(tag) or "").strip()


def title(name):
    return " ".join(word.capitalize() for word in re.split(r"[-_ ]+", name))


def first_sentence(overview):
    match = re.match(r"(.+?[.!?])(\s|$)", overview, re.S)
    return " ".join((match.group(1) if match else overview).split())


apps = []
for path in sorted(ROOT.glob("*.xml")):
    root = ET.parse(path).getroot()
    if root.tag != "Container":
        continue  # ca_profile.xml and anything else that isn't a template
    name = text(root, "Name") or path.stem
    apps.append({
        "file": path.name,
        "name": name,
        "title": title(name),
        "project": text(root, "Project"),
        "description": first_sentence(text(root, "Overview")).replace("|", "\\|"),
    })

lines = [
    "# dodert's Unraid templates",
    "",
    "Templates for Unraid's Community Applications.",
    "",
    "| App | Description |",
    "|---|---|",
]
for app in apps:
    link = f"[{app['title']}]({app['project']})" if app["project"] else app["title"]
    lines.append(f"| {link} | {app['description']} |")
lines += [
    "",
    "## Install",
    "",
    "Unraid removed the \"Template repositories\" setting in 6.10, so each template is installed with one command",
    "in the Unraid terminal (run it again to update the template). Then pick the app in **Docker → Add Container**.",
    "",
]
for app in apps:
    lines += [
        f"**{app['title']}**",
        "",
        "```bash",
        f"mkdir -p /boot/config/plugins/dockerMan/templates-user && curl -fsSL {RAW}/{app['file']} -o /boot/config/plugins/dockerMan/templates-user/my-{app['file']}",
        "```",
        "",
    ]
lines += [
    "To list them in **Apps → Private** (Community Applications) instead, download them to",
    "`/boot/config/plugins/community.applications/private/dodert/`.",
    "",
    "Each template and its icon are copied automatically from the app's repository (`unraid/` folder); change them there.",
    "This README is rebuilt from the templates by the *Update README* workflow.",
    "",
]
(ROOT / "README.md").write_text("\n".join(lines), encoding="utf-8")
print(f"README.md: {len(apps)} templates")
