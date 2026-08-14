# Partner workflow

The website is separate from the game repository. That lets either partner edit
the public site without needing administrative access to the Quest source or its
release settings.

## Normal change

1. Pull the latest `main`.
2. Create a short branch such as `site/battle-art-update`.
3. Edit only what the task requires.
4. Preview `public/index.html` locally at desktop and mobile widths.
5. Confirm every public link works and no private or copyrighted files were added.
6. Open a pull request into `main` and describe the visible change.
7. Merge after the checks pass. GitHub Pages deploys automatically.

## Content rules

- Treat progress percentages and performance numbers as dated estimates, not promises.
- Link downloads to official GitHub Releases rather than third-party mirrors.
- Never include ROMs, extracted ROM caches, saves, signing keys, access tokens, or commercial assets.
- Credit upstream Gen1Recomp and individual mod authors. Do not imply ownership of their work.
- Keep the fan-project and non-affiliation notice visible.
- Do not change the Pages workflow, repository permissions, domains, or security settings unless both maintainers understand the reason.

## AI-agent rules

An AI agent should inspect the current files and `git diff` before editing, preserve
unrelated work, and never push, merge, publish, change permissions, or upload files
unless its user explicitly authorizes that action.
