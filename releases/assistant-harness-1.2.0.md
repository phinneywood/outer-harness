# Outer Harness 1.2.0 distribution

The existing `assistant-harness` package identity now includes `outer-harness` as its primary entry point and displays as Outer Harness. Its five focused references cover configuration, onboarding, projects, knowledge and scheduled use. The four legacy skill paths remain byte-for-byte unchanged for existing consumers, including the advanced `harness-audit` utility.

## Archive and source

- Archive: `releases/assistant-harness-1.2.0.zip`.
- SHA-256: `ebca8f18d0b9dddb289f123a432d59d6cf0cdad254be615ef991894e14d9ef43`.
- Entry-point source: the merged simplification in `9c8353e78a44cc15659a554f57bb72b5fc8ddb2b`, with UI metadata added by this distribution change.
- Core SKILL.md SHA-256: `5b31693be23607d301a15b6317c2b4075e275237d084fc760cc0b8fa8a0e732e`.
- Reviewed package list: `plugins/assistant-harness/package-files.json`; archive entries exactly match it plus the root manifest.
- No private configuration, task registrations, rollback prompts, connection IDs or credentials are included.

Reproduce with `python3 scripts/build_plugin.py assistant-harness`. The repository workflow compares the resulting archive with this saved release. Historical archives remain unchanged.

## Verification scope

- All 34 repository tests passed locally. They cover configuration behavior, package scope/source bytes/reproducibility, reference resolution and offline registration-preservation checks.
- The native skill validator passed on the actual personal-skill candidate. The package convention checker passed on the extracted archive with no errors. That checker does not validate the complete external plugin schema.
- Two independent read-only model checks exercised scoped recovery and a blocked task migration. See [observed behavior](assistant-harness-1.2.0-behavior-checks.md).
- A controlled missing-reference retrieval returned GitHub 404. No dependent operational write or checkpoint advance was performed. Source saving and packaging were independently supported work.
- The personal skill was saved through the supported native workflow; persisted core and reference bytes were compared with source. Native reader discovery/loading in the originating session remains a separate gate.
- Cloud upload, fresh ordinary Chat loading of every required reference, iOS loading, automatic activation, controlled operational-write/repeat behavior and independent scheduled execution are not established by this archive.

## Upgrade boundary

Upload this version through the existing plugin identity; do not create a second enabled plugin. Repository changes and personal-skill saving do not update the installed cloud plugin.

Preserve the existing private configuration and all native registrations. Before migrating any prompt, obtain its complete runtime/binding/delivery metadata, preserve full event filters, verify actual runtime loading and behavior, retain private rollback evidence, and read the changed registration back. Migrate one registration at a time; keep the daily single exception-only reporter, distinct hourly scopes and specialty workflows. Incomplete event-filter evidence blocks Gmail migration. Do not retire compatibility paths until every consumer has independent verification.

The public README and historical first-run guide still describe the previously verified 1.1.1 package. This distribution record is not a claim that live consumers were upgraded.
