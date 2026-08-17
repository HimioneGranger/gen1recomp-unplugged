# Gen1Recomp VR Unplugged — website source only

> [!IMPORTANT]
> This is **not a second game project**, and development is **not moving here**.
> The single project repository for code, APK releases, issues, and roadmap work is
> [Gen1recomp-Quest-Standalone](https://github.com/HimioneGranger/Gen1recomp-Quest-Standalone).

This repository contains only the public website for **Gen1Recomp VR Unplugged**.
It is deliberately plain HTML and CSS so either project partner can update the
site without installing a framework or build tool.

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

Game code, launcher code, mod integration, release assets, and project issues do
not belong in this repository. Put that work in the
[main Quest project](https://github.com/HimioneGranger/Gen1recomp-Quest-Standalone).

See [COLLABORATING.md](COLLABORATING.md) for the partner workflow.
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
