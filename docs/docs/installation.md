---
title: Installation
description: How to install mpesakit using pip and virtual environments.
slug: /installation
sidebar_label: Installation
tags:
   - installation
   - setup
   - pip
---

### Install via PyPI

Install mpesakit from PyPI with pip.

Quick install (system or virtual environment):

```bash
pip install mpesakit
```

Recommended (create and use a virtual environment):

```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

pip install --upgrade pip
pip install mpesakit
```

Verify installation:

```bash
pip show mpesakit
```
