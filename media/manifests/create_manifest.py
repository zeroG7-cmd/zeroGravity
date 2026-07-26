#!/usr/bin/env python3
"""Create a new project media manifest.

The manifest is the ONLY thing that goes in git for a video project -
the actual footage stays on your media drive, referenced by media_root.
Run this from the zeroGravity repo root:

    python media/manifests/create_manifest.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

MANIFESTS_DIR = Path(__file__).resolve().parent
TEMPLATE_PATH = MANIFESTS_DIR / "project_manifest.template.json"


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or "untitled-project"


def ask(prompt: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    value = input(f"{prompt}{suffix}: ").strip()
    return value or default


def ask_yes_no(prompt: str, default: bool = False) -> bool:
    default_label = "Y/n" if default else "y/N"
    value = input(f"{prompt} ({default_label}): ").strip().lower()
    if not value:
        return default
    return value.startswith("y")


def next_project_id() -> str:
    existing = sorted(MANIFESTS_DIR.glob("ZG-MEDIA-*.json"))
    numbers = []
    for path in existing:
        match = re.search(r"ZG-MEDIA-(\d+)", path.stem)
        if match:
            numbers.append(int(match.group(1)))
    next_number = (max(numbers) + 1) if numbers else 1
    return f"ZG-MEDIA-{next_number:03d}"


def main() -> None:
    print("New project manifest\n" + "-" * 30)

    title = ask("Project title (e.g. 'Riverside B&B promo shoot')")
    slug = slugify(ask("Slug for folder naming", slugify(title)))
    project_id = next_project_id()

    print("\nStatus options: shooting / editing / delivered / archived")
    status = ask("Current status", "editing")

    media_drive = ask("Media drive root (where the actual footage lives)", "D:/ZeroGravity-Media")
    media_root = f"{media_drive}/projects/{slug}"

    print("\nRoles (comma separated, e.g. drone operator, camera operator)")
    role_input = ask("Your role(s) on this project", "drone operator")
    roles = [r.strip() for r in role_input.split(",") if r.strip()]

    captured_by_zg = ask_yes_no("Was this captured by zeroGravity (not stock/third-party)?", True)
    third_party = ask_yes_no("Does it include any third-party material?", False)

    print("\nRights - be honest here, this protects you legally")
    client_permission = ask("Client permission to use footage at all (yes/no/unknown)", "unknown")
    portfolio_permission = ask("Client permission to show this on your PUBLIC portfolio (yes/no/unknown)", "unknown")
    release_notes = ask("Any notes on rights/permissions (optional)", "")

    website_ready = ask_yes_no("Ready to feature on the website right now?", False)
    if website_ready and portfolio_permission.lower() != "yes":
        print("\nNote: you said website_ready=yes but portfolio_permission isn't 'yes'.")
        print("Setting website_ready to False until permission is confirmed - safer default.")
        website_ready = False

    manifest = {
        "project_id": project_id,
        "title": title,
        "status": status,
        "media_root": media_root,
        "role": roles,
        "ownership": {
            "captured_by_zeroGravity": captured_by_zg,
            "third_party_material": third_party,
        },
        "rights": {
            "client_permission": client_permission,
            "portfolio_permission": portfolio_permission,
            "release_notes": release_notes,
        },
        "collaborators": [],
        "deliverables": [],
        "website_ready": website_ready,
    }

    output_path = MANIFESTS_DIR / f"{project_id}-{slug}.json"
    output_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print(f"\nCreated: {output_path}")
    print(f"Remember to actually create the media folder at: {media_root}")


if __name__ == "__main__":
    main()