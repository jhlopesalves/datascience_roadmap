import os
import posixpath

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

    _BUNDLE_LABELS = {
        "bundle_boosting": "Boosting (HGBT, LightGBM)",
        "bundle_calibration": "Calibration",
        "bundle_capstone_core": "Capstone Core",
        "bundle_causal": "Causal Inference",
        "bundle_dl_texts": "DL Texts",
        "bundle_embeddings_search": "Dense Representations & Semantic Search",
        "bundle_fairness_calibration": "Fairness & Calibration",
        "bundle_foundations": "Foundations",
        "bundle_fpp3": "FPP3 (Forecasting)",
        "bundle_glm": "Generalised Linear Models",
        "bundle_hf_transformers": "HF Transformers",
        "bundle_keras_tf": "Keras & TensorFlow",
        "bundle_linear_algebra": "Linear Algebra",
        "bundle_metrics": "Metrics",
        "bundle_ml_product": "ML Product & Demos",
        "bundle_mlops_hygiene": "MLOps Hygiene",
        "bundle_model_selection": "Model Selection",
        "bundle_monitoring": "Production Monitoring",
        "bundle_nlp_foundations": "NLP Foundations",
        "bundle_onnx": "ONNX Export",
        "bundle_orchestration_tracking": "Orchestration & Tracking",
        "bundle_peft_quant": "PEFT & Quantisation",
        "bundle_prophet": "Prophet",
        "bundle_pytorch_core": "PyTorch Core",
        "bundle_rag_eval": "RAG Evaluation",
        "bundle_rag_orchestration": "RAG Orchestration",
        "bundle_regularisation": "Regularisation",
        "bundle_responsible_ai": "Responsible AI",
        "bundle_scaling_data": "Scaling Data (Dask/DuckDB)",
        "bundle_serving_api": "Serving APIs",
        "bundle_serving_llm": "Serving LLMs",
        "bundle_sklearn_core": "scikit-learn Core",
        "bundle_sktime_darts": "sktime & Darts",
        "bundle_stats_core": "Statistics Core",
        "bundle_stats_inference": "Statistical Inference",
        "bundle_statsmodels_ts": "statsmodels Time Series",
        "bundle_svm_knn": "SVM & k-NN",
        "bundle_trees_forests": "Trees & Forests",
        "bundle_unsupervised_repr": "Unsupervised Representations",
    }

    def _format_bundle_name(bundle_id: str) -> str:
        if bundle_id in _BUNDLE_LABELS:
            return _BUNDLE_LABELS[bundle_id]
        label = bundle_id
        if label.startswith("bundle_"):
            label = label[len("bundle_") :]
        label = label.replace("_", " ").title()
        replacements = {
            "Mlops": "MLOps",
            "Mlflow": "MLflow",
            "Onnx": "ONNX",
            "Svm": "SVM",
            "Knn": "k-NN",
            "Hgbt": "HGBT",
            "Pca": "PCA",
            "Nmf": "NMF",
            "Kmeans": "KMeans",
            "Arima": "ARIMA",
            "Sarimax": "SARIMAX",
            "Fpp3": "FPP3",
            "Sktime": "sktime",
            "Dowhy": "DoWhy",
            "Econml": "EconML",
            "Fastapi": "FastAPI",
            "Tensorflow": "TensorFlow",
            "Nlp": "NLP",
            "Dl": "DL",
            "Hf": "HF",
            "Peft": "PEFT",
            "Lora": "LoRA",
            "Llm": "LLM",
            "Llms": "LLMs",
            "Rag": "RAG",
            "Api": "API",
            "Ml": "ML",
            "Eval": "Evaluation",
        }
        for src, target in replacements.items():
            label = label.replace(src, target)
        return label

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
        checklist_items = [
            "- [ ] Code daily (≥60 min)",
            "- [ ] Math/stats micro (20–30 min)",
            "- [ ] Reading (10–20 min)",
            "- [ ] Push MLflow runs",
            "- [ ] Update progress",
        ]
        for bundle in w.get("bundles", []) or []:
            checklist_items.append(
                f"- [ ] Review bundle: {_format_bundle_name(bundle)}"
            )
        parts.append(
            "\n---\n**Checklist**\n\n" + "\n".join(checklist_items) + "\n"
        )
        return "\n".join([p for p in parts if p])

    def _relative_url(target):
        page = env.variables.get("page")
        page_file = getattr(page, "file", None) if page else None
        page_src = getattr(page_file, "src_uri", "") if page_file else ""
        if not page_src:
            return target

        base_dir = posixpath.dirname(page_src)
        href = posixpath.relpath(target, base_dir or ".")
        if href == ".":
            href = "./"
        return href

    def week_toc():
        lines = []
        phases = {}
        for k, v in weeks.items():
            phases.setdefault(v.get("phase", "Unsorted"), []).append(v)
        for phase, items in phases.items():
            items = sorted(items, key=lambda x: x["number"])
            lines.append(f"### {phase}\n")
            for it in items:
                target = f"roadmap/week-{it['number']:02d}.md"
                href = _relative_url(target)
                lines.append(
                    f"- [Week {it['number']:02d} — {it['title']}]({href})"
                )
            lines.append("\n")
        return "\n".join(lines)

    env.macro(render_week)
    env.macro(week_toc)
