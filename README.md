# Data Science Roadmap — Jhonatan

A book‑style roadmap built with **MkDocs Material**, designed for clarity, rigour, and easy publishing via **GitHub Pages**.

## Quick start

1. Create a new GitHub repository and push these files.
2. Edit `mkdocs.yml` to set your `site_url` and `repo_url`.
3. Enable **Pages** in your repo (Settings → Pages → Build and deployment → GitHub Actions).
4. Push to `main`. The included workflow builds and deploys automatically.

## Local preview

```bash
pip install -r requirements.txt
mkdocs serve
```

Then open <http://127.0.0.1:8000/>.

## Content model

- Edit week content in `docs/data/weeks.yaml`. Each week page can be rendered with `{{ render_week(n) }}`.
- Add resources in `docs/data/resources.yaml`.
- Create more pages in `docs/roadmap/` as needed (copy `week-01.md` and change the number).
- Custom CSS/JS live in `docs/assets/`.

## Why MkDocs Material?

- Beautiful typography and search out of the box
- First‑class Markdown features (admonitions, tabs, callouts)
- Simple CI/CD for GitHub Pages
- Extensible via the `macros` plugin for data‑driven pages