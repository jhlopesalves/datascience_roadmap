import os

import yaml


def _load_yaml(rel_path):
    here = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(here, "docs", "data", rel_path)
    with open(data_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def define_env(env):
    weeks = _load_yaml("weeks.yaml")
    resources = _load_yaml("resources.yaml")
    env.variables["weeks"] = weeks
    env.variables["resources"] = resources

    def render_week(week_no):
        w = weeks.get(str(week_no))
        if not w:
            return f"**Week {week_no}** — TBD"

        def sec(title, body):
            return f"\n### {title}\n\n{body.strip()}\n" if body else ""

        parts = [f"## Week {w['number']:02d} — {w['title']}\n"]
        parts.append(sec("Code focus", w.get("code_focus", "")))
        parts.append(sec("Math & stats", w.get("math_stats", "")))
        parts.append(sec("Bibliography (specific)", w.get("bibliography", "")))
        parts.append(sec("Docs (official)", w.get("docs", "")))
        proj = w.get("project", {})
        if proj:
            p = []
            if proj.get("title"):
                p.append(f"**Title:** {proj['title']}")
            if proj.get("dataset"):
                p.append(f"**Dataset:** {proj['dataset']}")
            if proj.get("metrics"):
                p.append(f"**Targets/metrics:** {proj['metrics']}")
            parts.append("\n## Project\n" + "  \n".join(p) + "\n")
        parts.append(sec("Summary", w.get("summary", "")))
        parts.append(
            "\n---\n**Checklist**\n- [ ] Code daily (≥60 min)\n- [ ] Math/stats micro (20–30 min)\n- [ ] Reading (10–20 min)\n- [ ] Push MLflow runs\n- [ ] Update progress\n"
        )
        return "\n".join([p for p in parts if p])

    def week_toc():
        lines = []
        phases = {}
        for k, v in weeks.items():
            phases.setdefault(v.get("phase", "Unsorted"), []).append(v)
        for phase, items in phases.items():
            items = sorted(items, key=lambda x: x["number"])
            lines.append(f"### {phase}\n")
            for it in items:
                anchor = f"week-{it['number']:02d}"
                lines.append(
                    f"- [Week {it['number']:02d} — {it['title']}](/roadmap/week-{it['number']:02d}/)"
                )
            lines.append("\n")
        return "\n".join(lines)

    env.macro(render_week)
    env.macro(week_toc)
