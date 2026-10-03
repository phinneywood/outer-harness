# Release checklist

- [ ] Record host/mode and source revision; inspect repository instructions.
- [ ] Resolve installed identity before deciding create versus update.
- [ ] Define a realistic task, boundary task, and observable success criteria.
- [ ] Keep methodology in canonical skill files; avoid host-specific duplicates.
- [ ] Run the host validator on the actual installation candidate.
- [ ] Run the bundled package checker and inspect all errors.
- [ ] Exercise helpers with valid and invalid fixtures.
- [ ] Inspect the diff; exclude credentials, private test data, and caches.
- [ ] Save source and install through separately supported paths.
- [ ] Compare persisted installation bytes against the pinned source.
- [ ] Prove native catalog discovery and reader loading with tool returns.
- [ ] Test behavior after loading; retain outputs and source-quality limits.
- [ ] Record each gate separately. Do not infer mobile support from Work.

The checker supports a narrow skills-only layout. It checks names, frontmatter, local resource links, file hashes, and selected manifest consistency rules. It does not validate the complete Agent Plugins schema, execute scripts, certify safety, install anything, or verify runtime behavior.

Consult current host instructions first, then official documentation when needed:
- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/deploy/connect-chatgpt
- https://help.openai.com/en/articles/20001066-skills-in-chatgpt
