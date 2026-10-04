# Assistant Harness 1.1.1 — packaging and first-run clarity

The four core skill instructions are unchanged from 1.1.0. This patch includes the root MIT license in the core ZIP, uses reviewed file lists for package building, and provides a plain-language overview, worked example, glossary and read-only first-run route.

## Reproduce the package

Use Python 3.10 or newer, from this repository:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/build_plugin.py assistant-harness
```

Compare the generated `dist/assistant-harness-1.1.1.zip` with the committed archive in this folder. No package installation, credentials or connected accounts are needed for these commands.

## Observed checks

- Seventeen local tests passed: nine configuration/renderer tests and eight archive tests.
- Ten core archive entries: manifest, root license, and four skills with their interface metadata.
- Archive tests compare each packaged file with its source bytes and check repeatable builds, rejection of symlinks/escaping paths, required license inclusion, exclusion of an unreviewed configuration file, and matching skill selection.
- The example configuration validates, grants no maintenance permissions, and identifies the current package version. Its source revision and service targets still require real private configuration.
- A read-only GitHub Actions workflow runs the tests and compares the rebuilt archive with the published ZIP. Its presence is not proof of a completed hosted run; inspect the linked commit's checks.
- Archive SHA-256: `8290f0d56da12129ffde77ce8b5f3476aad698d19cd9595dd5cb40a03e4e87b7`.

## Verification limits

These checks establish code and packaging behavior. They do not establish installation compatibility, independent scheduled execution, automatic activation, live connector writes or iOS behavior. See [1.1.0](assistant-harness-1.1.0.md) and [1.0.0](assistant-harness-1.0.0.md) for earlier evidence, within each record's scope.

GitHub source, uploaded plugins, personal Work skills and saved-task pins remain separate artifacts. This release does not update existing installations, task registrations, schedules or permissions. Historical ZIPs are retained unchanged; 1.1.1 is the core distribution with the included root license.
