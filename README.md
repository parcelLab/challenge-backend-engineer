# parcelLab — Returns Portal (Challenge Scaffold)

- [parcelLab — Returns Portal (Challenge Scaffold)](#parcellab--returns-portal-challenge-scaffold)
  - [📖 About the project and the use case](#-about-the-project-and-the-use-case)
  - [⚙️ Technical overview and instructions for developing](#️-technical-overview-and-instructions-for-developing)
  - [🏗️ Solving the Challenge and Rules to follow](#️-solving-the-challenge-and-rules-to-follow)
    - [IMPORTANT: Time limit](#important-time-limit)
    - [Use of AI and coding agents](#use-of-ai-and-coding-agents)
    - [1️⃣ Overall goal](#1️⃣-overall-goal)
    - [2️⃣ Backlog tasks to choose from](#2️⃣-backlog-tasks-to-choose-from)
    - [3️⃣ Deliverables](#3️⃣-deliverables)

## 📖 About the project and the use case

This is a synthetic, brownfield-style project to evaluate backend-focused product engineering skills in a returns domain. It simulates a simplified customer returns portal with dummy data and a minimal Django + HTMX UI.

You will work on a small Django app that mimics a returns portal. The core backend challenges are:
- mapping a raw order payload into a domain model
- designing and implementing a rules engine for return eligibility
- writing tests and making the suite pass

> Please do not fork this repository. Clone it, work locally, and submit either as a (non-forked) repository or a zip file.

## ⚙️ Technical overview and instructions for developing

**Stack:** Python 3.12+, Django, pytest + pytest-django, ruff, mypy. (PyYAML is included if you decide to store rules in YAML.)

### Getting started

```bash
# install deps (uv preferred)
uv venv
uv pip install -e ".[dev]"

# run tests
pytest

# run dev server
python manage.py runserver
```

Open <http://localhost:8000/returns/> and try order `RMA-1001` with email `alex@example.com` or zip `10115`.

### Structure

```bash
portal/
  data/orders_raw.json      # dummy orders (raw payload)
  data/                     # your rules config goes here (you define the structure)
  services/mapper.py        # map raw payload -> domain model (intentionally incomplete)
  services/eligibility.py   # rules loader + evaluator (stubbed)
  templates/returns/*       # minimal UI (Django + HTMX)
  tests/*                   # pytest tests (some intentionally failing)
```

## 🏗️ Solving the Challenge and Rules to follow

### IMPORTANT: Time limit

> 💡 Please do not spend more than **4 hours**. If you reach the limit, stop and submit what you have. We value good time management and transparency.

### Use of AI and coding agents

AI tools are allowed. If you use them, document prompts and outputs in `AI_LOG.md`.

### 1️⃣ Overall goal

Pick from the tasks below to improve the project according to your time budget and priorities. You **do not** have to implement all tasks. Prioritize what you think best demonstrates your skills and explain your choices in `DECISIONS.md`.

### 2️⃣ Backlog tasks to choose from

#### BR-001 Complete the mapper gaps (Core)
The mapper currently does not populate key item attributes. Complete the mapping so item flags can be used by your rules engine.

Missing fields:
- `is_digital`
- `is_final_sale`
- `category`

#### BR-002 Implement a return eligibility engine (Core)
Design your own rules structure (JSON/YAML/etc.) and implement the evaluation engine. We intentionally do **not** provide a rules file to avoid biasing your approach.

The evaluator should return a clear result per item (returnable, flag, reason, matched rule) and support at minimum:
- Return window (based on delivered date + return window days)
- Already returned (quantity returned >= quantity)
- Digital item
- Final sale item

#### BR-003 Add/extend tests for rules + mapper (Core)
Add unit tests that cover your mapper changes and eligibility rules. The goal is to make the test suite pass and demonstrate good testing practices.

#### FR-001 Minimal UX improvement: filter returnable items
The UI includes a small HTMX “Recompute” action. Extend it to support a “Show returnable only” filter and update the response accordingly.

#### OPEN-001 Surprise us
Add a small feature, polish detail, or improvement that shows initiative. Keep it scoped and document your reasoning in `DECISIONS.md`.

### 3️⃣ Deliverables

Provide a zip file or a link to your private repository containing:

- Working code that is error-free, type-safe, and well-structured
- Commits in small, readable steps
- A log of AI usage in `AI_LOG.md` (if applicable)
- A brief summary of decisions and tradeoffs in `DECISIONS.md`

---

© parcelLab — May your rules be correct and your returns always smooth.
