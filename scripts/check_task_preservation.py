#!/usr/bin/env python3
"""Offline metadata guard for reviewed task-prompt migrations; performs no writes.

Input objects are complete host registration snapshots. Missing metadata blocks
validation. Passing this guard does not prove semantic equivalence or execution.
"""
import argparse
import json
from pathlib import Path

REQUIRED = ("id", "title", "prompt", "schedule", "default_timezone", "timing_mode",
            "is_enabled", "runtime", "conversation_id", "notifications_enabled",
            "email_enabled")
VOLATILE = {"updated_at", "last_run_time", "last_run_status", "next_run_time"}


def check(before: dict, after: dict, expected_prompt: str, *, event: bool = False) -> list[str]:
    """Return blocking errors; compare unknown host fields as well as known ones."""
    if not isinstance(before, dict) or not isinstance(after, dict):
        return ["Both snapshots must be objects"]
    errors = []
    for label, snapshot in (("before", before), ("after", after)):
        for key in REQUIRED:
            if key not in snapshot or snapshot[key] is None:
                errors.append(f"{label}: missing {key}")
        for key in ("id", "title", "prompt", "schedule", "default_timezone", "timing_mode",
                    "runtime", "conversation_id"):
            if key in snapshot and (not isinstance(snapshot[key], str) or not snapshot[key].strip()):
                errors.append(f"{label}: invalid {key}")
        for key in ("is_enabled", "notifications_enabled", "email_enabled"):
            if key in snapshot and type(snapshot[key]) is not bool:
                errors.append(f"{label}: {key} must be boolean")
        is_event = event or "X-UNSCHEDULED" in str(snapshot.get("schedule", ""))
        if is_event:
            if not isinstance(snapshot.get("event_trigger"), dict) or not snapshot["event_trigger"]:
                errors.append(f"{label}: complete event_trigger required")
            if snapshot.get("event_trigger_complete") is not True:
                errors.append(f"{label}: event trigger coverage unverified")
    if not isinstance(expected_prompt, str) or not expected_prompt.strip():
        errors.append("A reviewed nonempty expected prompt is required")
    elif after.get("prompt") != expected_prompt:
        errors.append("Prompt does not match the reviewed replacement")
    for key in sorted((before.keys() | after.keys()) - VOLATILE - {"prompt"}):
        if key not in before or key not in after or before[key] != after[key]:
            errors.append(f"Preserved field changed: {key}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("before", type=Path)
    parser.add_argument("after", type=Path)
    parser.add_argument("expected_prompt", type=Path)
    parser.add_argument("--event", action="store_true")
    args = parser.parse_args()
    try:
        errors = check(json.loads(args.before.read_text()), json.loads(args.after.read_text()),
                       args.expected_prompt.read_text(), event=args.event)
    except (OSError, ValueError) as exc:
        print(json.dumps({"status": "blocked", "errors": [str(exc)]}))
        return 2
    print(json.dumps({"status": "blocked" if errors else "metadata_preserved",
                      "errors": errors,
                      "scope": "Metadata and exact reviewed prompt only; not semantic or runtime proof"}))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
