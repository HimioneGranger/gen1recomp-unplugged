# Gen1QuestVR Site

This is the public website for **Gen1Recomp VR Unplugged**. It is deliberately
plain HTML and CSS so either project partner can update it without installing a
framework or build tool.

Live site: `https://himionegranger.github.io/gen1recomp-unplugged/`

## Editing the site

All published files live in [`public/`](public/):

- `public/index.html` contains the words and page structure.
- `public/styles.css` contains the visual design and responsive layout.
- `public/assets/` contains local images.

For a quick local preview, open `public/index.html` in a browser. For a more
accurate preview, run a small static server from the repository root:

```sh
python -m http.server 8080 --directory public
```

Then open `http://localhost:8080`.

## Publishing

Every change merged to `main` that touches `public/` automatically deploys
through [the Pages workflow](.github/workflows/deploy-pages.yml). Do not commit
tokens, passwords, ROMs, extracted caches, saves, APK signing material, or
commercial game assets.

See [COLLABORATING.md](COLLABORATING.md) for the partner workflow.
