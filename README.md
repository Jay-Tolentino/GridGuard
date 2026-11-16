
# GridGuard

### Reliability Risk & Compliance Data Validator

GridGuard is a Python application that automates data validation for simulated electrical equipment risk assessments.

The project demonstrates how scripting, data analysis, and reporting can help identify inconsistencies in records used for reliability risk management.

**Disclaimer:** This is an independent educational project using synthetic data. It is not affiliated with SMUD and does not implement or certify compliance with NERC standards.

## Features

- Validates equipment risk scores using a demonstration formula.
- Detects missing and invalid risk inputs.
- Identifies duplicate equipment IDs.
- Flags missing, invalid, and future inspection dates.
- Stores validation findings in SQLite.
- Displays results in an interactive Streamlit dashboard.
- Exports validation findings to CSV and Excel.
- Includes automated tests using pytest.

## Technologies

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Pandas | Data processing and validation |
| SQLite | Local database storage |
| Streamlit | Interactive dashboard |
| OpenPyXL | Excel report generation |
| pytest | Automated testing |
| Git | Version control |

## How It Works

1. Equipment records are loaded from a synthetic CSV dataset.
2. The validation engine checks the records for inconsistencies.
3. Identified issues are saved to SQLite.
4. Streamlit displays validation findings and summary metrics.
5. Users can export reports for further review.

## Risk Scoring

For demonstration purposes:

Risk Score = Likelihood × Impact

Likelihood and impact must each be integers between 1 and 5.

This model is illustrative and is not an official utility risk assessment methodology.

## Getting Started

### Requirements

- Python 3.13
- Git

### Installation

Clone the repository:

```bash
git clone https://github.com/Jay-Tolentino/GridGuard.git
cd GridGuard
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

### Run the Application

```bash
python -m streamlit run app.py
```

Open http://localhost:8501 in your browser.

### Run Tests

```bash
python -m pytest -v
```

## Dataset

The included dataset contains fictional equipment records with intentional errors for testing.

No real utility operational data or internal compliance information is used.

## Future Improvements

- Add configurable validation rules.
- Track historical validation runs.
- Add additional automated tests.
- Expand data reconciliation across multiple sources.
- Explore anomaly detection using machine learning.

## Project Motivation

I developed GridGuard to explore how programming and automation can support reliability risk management and data quality.

My goal was to apply software engineering skills to a practical problem involving data accuracy, validation, and reporting.
