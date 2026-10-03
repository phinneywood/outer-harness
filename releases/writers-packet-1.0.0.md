# Writer’s Packet 1.0.0 — installed; automatic activation unresolved

Date: 2026-09-27
Skill source: `6cb309581b811e5812bac4e62b23c8f8447241b9`
Target: personal Work skill and separate ordinary Chat cloud plugin.

| Gate | Status | Evidence and scope |
| --- | --- | --- |
| Static validation | Passed | Host validator on managed candidate; package checker ok=true, no errors. No full-schema/security certification claimed. |
| Personal skill persisted | Passed | Supported save and reconciled remote path with matching SKILL.md hash. |
| Source equality | Passed for package | SKILL.md SHA-256 `39bd17730479ed99bedf6d0f06ce81bf381dc7c35f58cddf06d6661cd64cb6ac`; archive bytes matched source. Cloud skill body was also inspected through ordinary Chat’s Sources panel. No independent hash of server-stored plugin bytes is claimed. |
| Cloud archive | Installed | Version 1.0.0; ZIP SHA-256 `ccbdb4af3f013c1ec6dfc17c7cc644a858c409584ba174804dd892814dc44626`. After explicit approval, uploaded through Plugins → Personal → Add, then selected Install plugin. Detail page showed version 1.0.0 and Try in chat. |
| ChatGPT customization | Saved and verified | Authorial boundary saved, reopened, and compared. After automatic-use failure, strengthened it to require writers-packet and placed it first. All unrelated original customization preserved. |
| Fresh ordinary Chat discovery/read | Passed with UI evidence | Fresh web Chat found `skills://plugins/writers-packet/writers-packet`, exposed Writer’s Packet in its native Sources → Skills panel, and opened the complete installed skill body. A subsequent read reported `api_tool.read_resource` with `uri=skills://plugins/writers-packet/writers-packet/SKILL.md`, start_line=1, num_lines=200, and reproduced the exact scoped-drafting instruction absent from the prompt. Raw hidden tool traces are not independently exposed by this browser surface; evidence is the native skill-source panel plus the read result rendered in Chat. |
| Explicitly loaded Chat behavior | Core boundary cases passed | Portfolio/whitepaper/LinkedIn preparation, diagnostic critique, comparison without a third version, explicit rewrite, and assistant email draft. See raw fictional test transcript. |
| Automatic activation / global boundary | Failed | A plain fictional portfolio request produced publication prose. A real-project “Help me write a portfolio page…” request also drafted copy. Strengthening and moving the custom rule to the top did not fix a fresh-chat retest. Do not describe the global rule as reliably enforced. |
| iOS | Unverified | No fresh iOS test performed. Web success is not iOS proof. |

## Usage and remaining work

Verified route: explicitly ask to use Writer’s Packet, or select the installed plugin. Example: “Use Writer’s Packet to help me prepare a portfolio case study.”

Installation and explicit-load verification are complete. Reliable automatic use for ordinary writing prompts remains unresolved. Customization is a model instruction, and these tests showed it can be ignored. No product-level enforcement is claimed. Avoid repeated wording changes without a new diagnostic hypothesis. Test iOS separately.

The earlier upload-approval blocker was resolved by the owner’s explicit approval in the continuation. No new MCP service, executable helper, credential, or data access was added.

## Behavior evidence

- [Source-loaded Work forward tests](writers-packet-1.0.0-forward-tests.md).
- [Ordinary Chat fictional behavior transcript](writers-packet-1.0.0-chat-tests.txt).
- Actual ordinary Chat output satisfied the no-ghostwriting cases when explicitly loaded. It labeled supplied fictional facts “Verified facts” once and listed multiple questions, so evidence labeling and question count were imperfect; passing the core boundary is not a claim of perfect compliance.
- Real-project failure transcripts and private verification-chat pointers remain in the owner’s project records; they are not published here as authored portfolio prose.

## Attribution

Inspired by Thomas Ptacek’s [How To Write With An LLM](https://sockpuppet.org/blog/2026/09/17/how-to-write-with-an-llm/) (*A Final Ward*, September 17, 2026). SKILL.md distinguishes the preparation packet and scoped drafting exception as adaptations.

## Restore

Prior repository source: `8bab66fcbaf6fe812c8c84f61cb5a25c230195c2`. New plugin; no older cloud plugin version was replaced. Rebuild using the existing build_plugin.py and pinned manifest. Reverse the authorial-boundary customization only if the owner requests it.
