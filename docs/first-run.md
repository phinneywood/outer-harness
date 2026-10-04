# First run

There are two routes: inspect the local tools without connecting an account, or install the skills in ChatGPT and configure your own services. Start locally if you only want to understand the project.

## Try the local tools

Use Python 3.10 or newer. These scripts use the Python standard library; no Python packages, service credentials or connected accounts are required.

Download the repository with GitHub's **Code → Download ZIP** menu, unzip it, and open a terminal in that folder. A Git checkout also works. Run:

```sh
python3 scripts/harness_config.py examples/assistant-harness/config.example.json
python3 -m unittest discover -s tests -v
python3 scripts/build_plugin.py assistant-harness
```

The first command should report that the configuration is valid. The tests check configuration and archive behavior. The last command writes `dist/assistant-harness-1.1.1.zip` and prints its SHA-256 fingerprint. It should match the [release record](../releases/assistant-harness-1.1.1.md).

The example's account addresses, document IDs and source revision are placeholders. Validation proves its structure is acceptable; it does not make the targets usable or grant authority. The all-zero revision must be replaced with a real, verified source commit before use. On GitHub, open the repository’s latest commit, then copy its full 40-character SHA with the copy button beside the commit identifier. Use the commit you actually inspected, rather than a moving branch name.

To see the prompt renderer without running an assistant or contacting a service:

```sh
python3 scripts/harness_config.py examples/assistant-harness/config.example.json --render daily --locator https://github.com/example/knowledge/blob/main/systems/assistant-harness.json
```

This only prints text. The example targets and all-zero revision are placeholders; do not use the printed prompt to run a real task.

## Use it with ChatGPT

This route requires a ChatGPT account with the relevant installation and connected-service features. Account availability and device behavior need their own checks.

1. Download [Assistant Harness 1.1.1](../releases/assistant-harness-1.1.1.zip). The repository is called Outer Harness; the installed core package is called Assistant Harness.
2. Use ChatGPT's supported plugin archive upload flow. Personal Work skills are a separate installation route; do not assume installing one installs the other. See the [setup guide](assistant-harness.md#build-and-install) and its official documentation links.
3. Connect the services the workflow needs. This package does not connect accounts. The supported profile uses GitHub, Trello and assistant-owned Google services; it does not request personal Google account access.
4. Copy [the example config](../examples/assistant-harness/config.example.json) into a **private** GitHub repository. Replace the source targets and policy links with records you own and have authorized the assistant to use. Keep maintenance permissions `false` for the first check. Retain explicit approval for protected actions. Configuration is not a place to store credentials.
5. Supply the current policy records referenced by the configuration: project-management policy, knowledge rules, knowledge workflow and a checkpoint recording what has been verified. Start with the [minimal policy templates](../examples/assistant-harness/policy-templates.md), adapt them to your own sources, and create the four private records. They are required inputs, not documents bundled with this package. Validate your configured copy locally.
6. In a fresh Chat, explicitly select Assistant Harness and the needed service plugins. Supply your private `config_locator`, the HTTPS GitHub URL of that JSON file. Request a **read-only** recovery of one known project's current outcome and next action; require the assistant to report which records it read. Do not authorize updates in this check.
7. Compare the answer with those source records. Record actual installation, loading and read results privately. If a required connection or policy cannot load, leave dependent operations pending; a plausible answer is not a successful check.

Only after the read-only path works should you enable narrowly authorized maintenance and test a real write with readback. Schedules are a later step: preserve existing registrations and verify an independent execution. See [verification criteria](assistant-harness.md#verify).

## Build metadata

Each `plugins/<package>/package-files.json` lists the source files reviewed for distribution. The builder includes the package manifest and those files, including the root license. Adding a file to a skill directory does not silently add it to an archive. Review and update the list when an intentional new resource belongs in a package.

Version 1.1.1 changes distribution only: the four core skill instructions are unchanged from 1.1.0. Existing installations and saved-task source pins are not updated automatically by this checkout or archive.
