# UV: Modern Python Package and Project Manager

## Introduction

`uv` is a fast Python package and project manager developed by Astral. It is designed to replace and simplify several traditional Python tools, including:

* pip
* venv
* pip-tools
* virtualenv
* parts of Poetry

Built in Rust, `uv` offers significantly faster package installation, dependency resolution, and project management compared to traditional Python tooling.

---

# Why UV?

Traditional Python development often requires multiple tools:

```text
venv         → Create virtual environments
pip          → Install packages
pip freeze   → Export dependencies
pip-tools    → Dependency management
poetry       → Project management
```

Managing all these tools can become complex.

`uv` combines many of these features into a single, modern tool.

---

# Key Features

* Extremely fast package installation
* Built-in virtual environment management
* Dependency resolution and locking
* Project initialization
* Python version management
* Compatible with existing pip workflows
* Supports `requirements.txt`
* Supports `pyproject.toml`
* Cross-platform support

---

# Installing UV

## Linux/macOS

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## Windows (PowerShell)

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

---

## Using pip

```bash
pip install uv
```

Verify installation:

```bash
uv --version
```

---

# Initializing a New Project

Create a new project:

```bash
uv init myproject
```

Project structure:

```text
myproject/
├── pyproject.toml
├── README.md
├── src/
└── .python-version
```

The generated `pyproject.toml` stores project metadata and dependencies.

---

# Creating a Virtual Environment

Traditional approach:

```bash
python -m venv .venv
```

UV approach:

```bash
uv venv
```

This creates:

```text
.venv/
```

---

# Activating the Virtual Environment

## Windows

```powershell
.venv\Scripts\activate
```

---

## Linux/macOS

```bash
source .venv/bin/activate
```

After activation:

```text
(.venv) $
```

appears in your terminal.

---

# Installing Packages

Traditional pip:

```bash
pip install requests
```

Using UV:

```bash
uv add requests
```

Benefits:

* Installs package
* Updates `pyproject.toml`
* Updates lock file automatically

---

# Installing Multiple Packages

```bash
uv add pandas numpy matplotlib
```

---

# Installing Development Dependencies

```bash
uv add --dev pytest black ruff
```

Development dependencies are stored separately.

---

# Removing Packages

```bash
uv remove requests
```

This removes:

* Package installation
* Dependency entry
* Lock file entry

---

# Running Python Scripts

Traditional:

```bash
python main.py
```

Using UV:

```bash
uv run main.py
```

Example:

```bash
uv run chatbot.py
```

---

# Running Python Commands

```bash
uv run python
```

Launches an interactive Python interpreter inside the project environment.

---

# Synchronizing Dependencies

Install all dependencies defined in the project:

```bash
uv sync
```

Equivalent to:

```bash
pip install -r requirements.txt
```

but uses the lock file for reproducible installs.

---

# Working with requirements.txt

Install from a requirements file:

```bash
uv pip install -r requirements.txt
```

Generate requirements file:

```bash
uv pip freeze > requirements.txt
```

UV maintains compatibility with traditional pip workflows.

---

# Lock Files

Generate a lock file:

```bash
uv lock
```

Lock files ensure:

* Consistent package versions
* Reproducible builds
* Team-wide dependency consistency

---

# Upgrading Dependencies

Upgrade all packages:

```bash
uv lock --upgrade
```

Upgrade a specific package:

```bash
uv add requests --upgrade-package requests
```

---

# Python Version Management

Install a Python version:

```bash
uv python install 3.12
```

List installed versions:

```bash
uv python list
```

Use a specific version:

```bash
uv venv --python 3.12
```

---

# Example Workflow

Create a new project:

```bash
uv init chatbot
cd chatbot
```

Create virtual environment:

```bash
uv venv
```

Install dependencies:

```bash
uv add langchain openai
```

Run application:

```bash
uv run main.py
```

Synchronize dependencies:

```bash
uv sync
```

---

# Project Structure Example

```text
chatbot/
├── .venv/
├── src/
│   └── main.py
├── pyproject.toml
├── uv.lock
└── README.md
```

---

# UV vs pip

| Feature              | pip      | uv        |
| -------------------- | -------- | --------- |
| Package Installation | Yes      | Yes       |
| Virtual Environments | No       | Yes       |
| Dependency Locking   | No       | Yes       |
| Project Management   | No       | Yes       |
| Python Management    | No       | Yes       |
| Speed                | Moderate | Very Fast |

---

# UV vs Poetry

| Feature               | Poetry   | uv        |
| --------------------- | -------- | --------- |
| Dependency Management | Yes      | Yes       |
| Lock Files            | Yes      | Yes       |
| Virtual Environments  | Yes      | Yes       |
| Python Management     | Limited  | Yes       |
| Performance           | Moderate | Very Fast |
| Simplicity            | Moderate | High      |

---

# Common Commands

| Task                         | Command                     |
| ---------------------------- | --------------------------- |
| Initialize Project           | `uv init project_name`      |
| Create Virtual Environment   | `uv venv`                   |
| Add Dependency               | `uv add package_name`       |
| Add Dev Dependency           | `uv add --dev package_name` |
| Remove Dependency            | `uv remove package_name`    |
| Run Script                   | `uv run script.py`          |
| Install Project Dependencies | `uv sync`                   |
| Generate Lock File           | `uv lock`                   |
| Upgrade Dependencies         | `uv lock --upgrade`         |
| Install Python Version       | `uv python install 3.12`    |
| List Python Versions         | `uv python list`            |

---

# Best Practices

1. Use `uv init` for new projects.
2. Keep dependencies in `pyproject.toml`.
3. Commit `uv.lock` to version control.
4. Use `uv sync` when cloning projects.
5. Add `.venv/` to `.gitignore`.
6. Use development dependencies for testing and linting tools.

Example `.gitignore`:

```gitignore
.venv/
__pycache__/
*.pyc
.env
```

---

# Advantages of UV

* Extremely fast package installation
* Unified tooling experience
* Built-in dependency locking
* Python version management
* Modern project structure
* Reduced tooling complexity
* Better developer productivity

---

# Limitations

* Relatively new compared to pip
* Smaller ecosystem than Poetry
* Some advanced Poetry workflows may not yet be available
* Teams may require migration from existing workflows

---

# Interview Definition

**UV** is a modern Python package and project manager developed by Astral. It combines package installation, dependency management, virtual environment creation, Python version management, and project tooling into a single high-performance tool, serving as a faster alternative to pip, venv, and parts of Poetry.

---

# One-Line Summary

**UV is an all-in-one, high-speed Python development tool that simplifies package management, virtual environments, dependency locking, and project setup while providing significantly faster performance than traditional Python tooling.**
