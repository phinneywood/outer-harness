# Outer Harness

Reusable operating skills for a ChatGPT assistant: recover context, maintain project and knowledge records, and audit the setup using existing connected services.

## What's here

| Source | Purpose |
| --- | --- |
| `skills/assistant-harness` | Recover authoritative context and route work |
| `skills/portfolio-pm` | Project reconciliation, daily briefings and completion checks |
| `skills/knowledge-reconcile` | Maintain external knowledge and organize assistant documents |
| `skills/harness-audit` | Configuration, installation, scheduling and repository audits |
| `skills/writers-packet` | Prepare evidence and questions for substantial writing |
| `skills/pocock-handoff` | Prepare a project handoff; retains upstream MIT license |
| `skills/distill` | Compress an answer into the essential points |
| `skills/chatgpt-plugin-factory` | Build, install and verify skill packages |
| `docs/`, `examples/`, `scripts/`, `tests/` | Setup, repository hygiene, private-config templates, package builder and fixtures |

The **Assistant Harness 1.0.0** plugin bundles the first four skills. Writer’s Packet and Pocock Handoff retain their own package manifests. Utility source in this repository does not add skills to an existing installed plugin.

## Get started

Read [setup and verification](docs/assistant-harness.md). Supply your own private configuration, current policies and authorized GitHub, Trello and assistant Google connections. Configuration examples contain placeholders and grant no maintenance permissions.

Build the core package:

```sh
python3 scripts/build_plugin.py assistant-harness --skills assistant-harness portfolio-pm knowledge-reconcile harness-audit
python3 -m unittest discover -s tests -p 'test_harness_config.py' -v
```

The verified package is also in [releases](releases/). Upload the archive through ChatGPT's plugin installation flow, or use the supported personal skill workflow in Work. Updating GitHub source does not update installed plugins, personal skills or saved task pins automatically. Keep one installation identity when upgrading.

The package contains no account connections, private policies, task registrations, credentials, server or database. Schedules are created separately in each user's account. Other personal reading, cleanup and specialty watches are outside the core package.

## Source ownership

This repository owns the harness and general assistant utilities. Long Form integrations belong with [Long Form](https://github.com/phinneywood/long-form), and strategy companions belong with [Strategy Factory](https://github.com/phinneywood/strategy-factory). The original [chatgpt-plugins collection](https://github.com/phinneywood/chatgpt-plugins) retains earlier releases during the transition.

See [the source migration record](docs/source-migration-2026-10-03.md) for provenance and verification limits. Fresh ordinary Chat reads were verified for 1.0.0; iOS, automatic activation and ordinary Chat mutation workflows remain separate checks.

## License and privacy

Original work is licensed under [MIT](LICENSE). Preserve the [Pocock Handoff upstream license](skills/pocock-handoff/LICENSE) when redistributing it.

Keep real configuration, document or board targets, full task prompts, rollback records and personal deployment links in a private repository. Follow the [repository hygiene procedure](docs/repository-hygiene.md) for ongoing checks.
