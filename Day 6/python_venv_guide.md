# Python Virtual Environment (venv) Guide

## Introduction

A virtual environment (`venv`) is an isolated Python environment that allows you to install and manage packages separately for each project. This helps prevent dependency conflicts between projects and keeps your system Python installation clean.

---

# Why Use a Virtual Environment?

Consider the following scenario:

* Project A requires Django 4.2
* Project B requires Django 5.1

If both versions are installed globally, they may conflict with each other.

A virtual environment provides each project with its own isolated set of dependencies.

### Without Virtual Environment

```text
System Python
│
├── Django 4.2
├── NumPy
└── Flask
```

All projects share the same packages.

### With Virtual Environment

```text
Project A
│
├── venv/
│   └── Django 4.2

Project B
│
├── venv/
│   └── Django 5.1
```

Each project has its own dependencies.

---

# Benefits of venv

* Dependency isolation
* Prevents package version conflicts
* Keeps system Python clean
* Easier project deployment
* Reproducible development environments

---

# Creating a Virtual Environment

Navigate to your project directory:

```bash
mkdir myproject
cd myproject
```

Create a virtual environment:

```bash
python -m venv venv
```

Alternatively:

```bash
python3 -m venv venv
```

This creates a directory named `venv`.

---

# Project Structure After Creation

```text
myproject/
│
├── venv/
│   ├── Scripts/      (Windows)
│   ├── bin/          (Linux/macOS)
│   └── Lib/
│
└── project_files/
```

---

# Activating the Virtual Environment

## Windows (Command Prompt)

```cmd
venv\Scripts\activate
```

## Windows (PowerShell)

```powershell
venv\Scripts\Activate.ps1
```

## Linux/macOS

```bash
source venv/bin/activate
```

After activation, your terminal prompt changes:

```text
(venv) $
```

The `(venv)` prefix indicates that the virtual environment is active.

---

# Installing Packages

Once activated, install packages using pip:

```bash
pip install requests
```

Install multiple packages:

```bash
pip install requests numpy pandas
```

View installed packages:

```bash
pip list
```

---

# Checking Package Information

```bash
pip show requests
```

Example output:

```text
Name: requests
Version: 2.32.3
Location: .../venv/lib/site-packages
```

---

# Saving Dependencies

Generate a requirements file:

```bash
pip freeze > requirements.txt
```

Example:

```text
requests==2.32.3
numpy==2.0.1
pandas==2.2.3
```

This file records all installed packages and versions.

---

# Installing Dependencies from requirements.txt

To recreate the environment on another machine:

```bash
pip install -r requirements.txt
```

This installs all required packages automatically.

---

# Upgrading pip

Keep pip updated:

```bash
python -m pip install --upgrade pip
```

---

# Deactivating the Virtual Environment

When you are finished working:

```bash
deactivate
```

The `(venv)` prefix disappears, indicating you have returned to the system Python environment.

---

# Deleting a Virtual Environment

Simply remove the venv directory:

## Windows

```cmd
rmdir /s venv
```

## Linux/macOS

```bash
rm -rf venv
```

No uninstall process is required.

---

# Common Commands Summary

| Task                   | Command                               |
| ---------------------- | ------------------------------------- |
| Create venv            | `python -m venv venv`                 |
| Activate (Windows CMD) | `venv\Scripts\activate`               |
| Activate (PowerShell)  | `venv\Scripts\Activate.ps1`           |
| Activate (Linux/macOS) | `source venv/bin/activate`            |
| Install package        | `pip install package_name`            |
| List packages          | `pip list`                            |
| Show package details   | `pip show package_name`               |
| Save dependencies      | `pip freeze > requirements.txt`       |
| Install dependencies   | `pip install -r requirements.txt`     |
| Upgrade pip            | `python -m pip install --upgrade pip` |
| Deactivate environment | `deactivate`                          |

---

# Example Workflow

```bash
# Create project directory
mkdir calculator
cd calculator

# Create virtual environment
python -m venv venv

# Activate environment
source venv/bin/activate

# Install packages
pip install numpy

# Verify installation
pip list

# Save dependencies
pip freeze > requirements.txt

# Exit environment
deactivate
```

---

# Best Practices

1. Create a virtual environment for every project.
2. Add `venv/` to `.gitignore`.
3. Store dependencies in `requirements.txt`.
4. Activate the environment before development.
5. Avoid installing project dependencies globally.

Example `.gitignore`:

```gitignore
venv/
__pycache__/
*.pyc
.env
```

---

# Interview Definition

**Virtual Environment (venv):**

> A virtual environment is an isolated Python environment that contains its own Python interpreter, libraries, and installed packages, allowing different projects to use different dependencies without conflicts.

---

# Conclusion

Python's `venv` module is an essential tool for managing project dependencies. It provides isolation, prevents version conflicts, improves reproducibility, and is considered a standard best practice for Python development.
