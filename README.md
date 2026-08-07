# Multi-Environment AI Configuration

A Python project demonstrating secure and maintainable application configuration management using environment variables and `python-dotenv`.

This project implements a configuration architecture where sensitive information and environment-specific settings are separated from application source code.

The main objective is to demonstrate how professional Python applications manage configuration in a scalable and secure way.

---

# Overview

Modern applications rarely run in only one environment. A typical application may have:

* Development environment
* Testing environment
* Production environment

Each environment can require different configuration values, such as:

* API keys
* Service endpoints
* Model configuration
* Database connection settings
* Feature flags

A common but problematic approach is storing configuration directly inside source code:

```python
OPENAI_API_KEY = "secret-key"
MODEL_NAME = "model-name"
```

This creates several issues:

* Sensitive data exposure
* Difficult environment switching
* Poor maintainability
* Increased risk when collaborating with other developers

This project applies a better approach:

> Configuration is externalized from application logic and managed through environment variables.

---

# Project Goals

This project was built to understand and implement:

* Environment variable management in Python
* Secure handling of sensitive configuration.
* Separation between configuration and business logic
* Centralized application settings management.
* Basic principles used in production Python applications.

---

# Architecture

The project follows a simple configuration flow:

```
.env
 |
 |  Load environment variables
 |
 ▼
config.py
 |
 |  Validate and expose configuration
 |
 ▼
main.py
 |
 |  Execute application logic
 |
 ▼
Application Output
```

---

# Design Principles

## 1. Separation of Concerns

Each file has a specific responsibility.

| File               | Responsibility                                            |
| ------------------ | --------------------------------------------------------- |
| `.env`             | Stores local configuration values and secrets             |
| `.env.example`     | Provides a safe configuration template                    |
| `config.py`        | Loads, validates, and manages configuration               |
| `main.py`          | Runs application logic using provided configuration       |
| `requirements.txt` | Defines project dependencies                              |
| `.gitignore`       | Prevents sensitive and generated files from being tracked |

---

## 2. Configuration Is Not Business Logic

The application logic should not know:

* where configuration comes from,
* how secrets are loaded,
* how environment variables are handled.

Instead:

```
main.py
   |
   ▼
config.py
   |
   ▼
environment variables
```

`main.py` only consumes configuration.

This makes the application easier to maintain and adapt across different environments.

---

# Project Structure

```
multi-environment-ai-configuration/

│
├── main.py
├── config.py
│
├── .env
├── .env.example
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Configuration Flow Explanation

## 1. Local Configuration (`.env`)

The `.env` file stores environment-specific values.

Example:

```env
OPENAI_API_KEY=your-api-key
BASE_URL=https://api.openai.com/v1
MODEL_NAME=gpt-5.5
ENVIRONMENT=development
```

This file is excluded from Git because it may contain sensitive information.

---

## 2. Configuration Management (`config.py`)

The configuration layer is responsible for:

* Loading environment variables.
* Reading configuration values.
* Validating required settings.
* Providing configuration to the application.

Example:

```python
from dotenv import load_dotenv
import os

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME")
```

The rest of the application does not directly interact with `.env`.

---

## 3. Application Layer (`main.py`)

The application only imports required configuration:

```python
from config import MODEL_NAME

print(MODEL_NAME)
```

`main.py` does not handle:

* `.env` loading,
* environment variable parsing,
* configuration validation.

This keeps application code clean and focused.

---

# Installation

## 1. Clone Repository

```bash
git clone <repository-url>

cd multi-environment-ai-configuration
```

---

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Configuration Setup

Create your local configuration file:

Copy:

```
.env.example
```

to:

```
.env
```

Then configure your values:

```env
OPENAI_API_KEY=your-secret-key
BASE_URL=https://api.openai.com/v1
MODEL_NAME=gpt-5.5
ENVIRONMENT=development
```

---

# Running the Application

Run:

```bash
python main.py
```

Example output:

```
=== AI Configuration Demo ===

Environment : development
Model       : gpt-5.5
Base URL    : https://api.openai.com/v1
API Key berhasil dimuat.
```

---

# Security Practices Applied

## 1. No Hard-Coded Secrets

Sensitive values are not stored inside Python files.

Avoid:

```python
OPENAI_API_KEY = "secret-key"
```

Instead:

```python
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
```

---

## 2. Sensitive Files Excluded From Git

The following files are ignored:

```
.env
.venv/
__pycache__/
```

Reasons:

* `.env` may contain secrets.
* `.venv` contains local dependencies.
* `__pycache__` contains generated Python bytecode.

---

# Technical Concepts Demonstrated

This project demonstrates practical understanding of:

* Python environment variables.
* Configuration management.
* Secure secret handling.
* Separation of concerns.
* Dependency management.
* Python project organization.
* Basic software architecture principles.

---

# Future Improvements

Possible improvements for a more advanced implementation:

* Replace manual configuration handling with `Pydantic Settings`.
* Add stronger configuration validation.
* Support multiple environments:

```
.env.development
.env.testing
.env.production
```

* Add automated testing.
* Add CI/CD workflow.
* Integrate cloud-based secret management.

---

# Learning Outcome

This project establishes the foundation for building scalable Python and AI applications.

The key architectural principle learned is:

> Application configuration should be externalized, centralized, validated, and separated from business logic.

This approach enables applications to run across different environments without modifying the source code.
