# Jhonatan’s Data-Science Roadmap (2025—)

A rigorous, practitioner-oriented programme designed for my own study: daily coding, applied mathematics and statistics, reproducible experiments, and ethically defensible deployment. This repository is **personal**, **opinionated**, and **auditable**. It houses weekly plans (currently Weeks 1–40), projects, reusable templates, and curated resources so that each session compounds into real-world competence.

---

## Purpose and design

I am training toward senior-level data-science practice with a blended focus:

- **Daily coding (Python-first):** scikit-learn, SciPy, statsmodels, Pingouin, PyTorch, Keras/TensorFlow, Hugging Face (Transformers, Datasets, PEFT), Dask, DuckDB, SQLAlchemy, FastAPI.
- **Applied maths & statistics alongside models:** linear algebra for optimisation, GLMs and deviance, time-series evaluation that respects temporal order, causality with assumptions made explicit.
- **Reproducibility & governance:** tests, seeds, MLflow tracking, model cards, subgroup-aware evaluation, and clear versioning.
- **Service thinking:** pipelines, packaging, APIs, monitoring, and graceful failure modes.

I study primarily in English; my daily environment is **VS Code + Jupyter/Colab (Pro when needed)**; I remain **cloud-agnostic** until later phases.

---

## Study cadence

- **Daily:** 60–90 minutes of coding; 20–30 minutes of mathematics/statistics; 10–20 minutes of reading (docs, book chapter, or paper); brief reflection.
- **Weekly:** one mini-project with explicit metric targets and a short write-up.
- **Phase ends:** a deployable artefact (service or library) with tests, a README, and a model card.

---

## Using this repository

### 1) Create a reproducible environment

```bash
# Option A: Pip
python -m venv .venv && source .venv/bin/activate
pip install --upgrade pip
pip install -r envs/requirements.txt

# Option B: Poetry
poetry install
poetry run pytest -q
````

### 2) Run a week locally

```bash
# Example: Week 13 (Boosting) project
cd projects/boosted-baselines
python -m src.train --config configs/hgb_lightgbm.yaml
```

### 3) Track experiments with MLflow

```bash
mlflow ui  # open http://127.0.0.1:5000 to inspect runs, params, metrics and artefacts
```

### 4) Serve a model (FastAPI template)

```bash
cd templates/fastapi
uvicorn app.main:app --reload
# GET /healthz for liveness; POST /predict with a JSON payload for inference
```

### 5) Mirror the plan into Notion (optional)

- Export weekly Markdown/CSV from `weeks/`, then **Import → Text & Markdown/CSV** in Notion.
- I keep a Notion database with relations: *Weeks* ↔ *Projects* ↔ *Resources* for quick filtering by topic or library.

---

## Conventions and governance

- **Versioning:** Semantic Versioning for the plan and templates (`MAJOR.MINOR.PATCH`).
- **Changelog:** Maintained in `CHANGELOG.md` (Keep a Changelog format).
- **Testing:** Each project includes unit tests for utilities, plus smoke tests for pipelines and endpoints.
- **Tracking:** All substantive runs log parameters, metrics, artefacts, and environments via MLflow.
- **Model Cards:** Substantial models include a brief `MODEL_CARD.md` with intended use, evaluation slices, calibration notes, and known failure modes.
- **Responsible AI:** Where relevant, I report subgroup metrics (fairlearn), reliability diagrams, and qualitative error analysis; I document constraints on use.

---

## Datasets

Datasets are **not** committed. Each project includes a small pull script or links to public sources (Kaggle, UCI, Hugging Face Datasets, public portals). Use the scripts to populate `data/` locally and respect dataset licences. Many tasks are reproducible with built-in loaders (e.g., scikit-learn, TorchVision, TFDS).

---

## Reference spine (selected)

- **Core docs:**
    scikit-learn • SciPy • statsmodels • PyTorch • Keras/TensorFlow • Hugging Face (Transformers, Datasets, PEFT) • Dask • DuckDB • SQLAlchemy • FastAPI • Prefect • Evidently • MLflow.

- **Texts & papers:**
    *An Introduction to Statistical Learning (ISLR)*; *The Elements of Statistical Learning (ESL)*; Murphy’s *Probabilistic Machine Learning*; Bishop’s *Pattern Recognition and Machine Learning*; Goodfellow–Bengio–Courville *Deep Learning*; *Dive into Deep Learning*; Kleppmann’s *Designing Data-Intensive Applications*; Mitchell et al., “Model Cards for Model Reporting”.

- **Operational references:**
    Semantic Versioning; Keep a Changelog; GitHub-Flavoured Markdown; Notion import guides.

For the complete, week-by-week reading lists and dataset links, open `weeks/` and the corresponding project folders.

---

## Style

* Formal, clear English; narrative first, code second.
* Prefer metrics aligned with the decision (e.g., deviance for GLMs; PR-AUC on imbalance; calibration when thresholds matter).
* Baselines before sophistication; ablations where they change decisions, not for page count.

---

## Contributing

This is primarily my study log. Corrections and improvements to reproducibility, robustness, or pedagogy are welcome—please keep changes focussed, with evidence and citations where appropriate.

---

## Licence

Unless otherwise stated, source code is released under the MIT Licence. Dataset use must comply with the original providers’ terms; some sub-projects include additional licences.

---

## Acknowledgements

Thanks to the open-source communities whose libraries make this work possible, and to the educators and researchers whose books and papers form the backbone of this roadmap.

---

### Useful links (quick access)

- scikit-learn: [https://scikit-learn.org/stable/user\_guide.html](https://scikit-learn.org/stable/user_guide.html)
- SciPy: [https://docs.scipy.org/doc/scipy/](https://docs.scipy.org/doc/scipy/)
- statsmodels: [https://www.statsmodels.org/stable/user-guide.html](https://www.statsmodels.org/stable/user-guide.html)
- PyTorch: [https://pytorch.org/tutorials/](https://pytorch.org/tutorials/)
- Keras/TensorFlow: [https://keras.io/](https://keras.io/) • [https://www.tensorflow.org/guide](https://www.tensorflow.org/guide)
- Hugging Face (Transformers / Datasets / PEFT): [https://huggingface.co/docs/transformers/](https://huggingface.co/docs/transformers/) • [https://huggingface.co/docs/datasets/](https://huggingface.co/docs/datasets/) • [https://huggingface.co/docs/peft/](https://huggingface.co/docs/peft/)
- Dask: [https://docs.dask.org/en/stable/](https://docs.dask.org/en/stable/) • DuckDB: [https://duckdb.org/docs/](https://duckdb.org/docs/)
- SQLAlchemy: [https://docs.sqlalchemy.org/en/20/](https://docs.sqlalchemy.org/en/20/)
- FastAPI: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
- Prefect: [https://docs.prefect.io/](https://docs.prefect.io/) • Evidently: [https://docs.evidentlyai.com/](https://docs.evidentlyai.com/) • MLflow: [https://mlflow.org/docs/latest/index.html](https://mlflow.org/docs/latest/index.html)
- Model Cards (paper): [https://arxiv.org/abs/1810.03993](https://arxiv.org/abs/1810.03993)
- Semantic Versioning: [https://semver.org/](https://semver.org/) • Keep a Changelog: [https://keepachangelog.com/](https://keepachangelog.com/)
- GitHub-Flavoured Markdown: [https://github.github.com/gfm/](https://github.github.com/gfm/)
- Notion import: [https://www.notion.so/help/import-data-into-notion](https://www.notion.so/help/import-data-into-notion)
  