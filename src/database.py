
from pathlib import Path
import sqlite3

import pandas as pd

# The database will be created inside the data folder.
DB_PATH = Path(__file__).resolve().parent.parent / "data" / "gridguard.db"


def save_validation_results(results):
    """Save validation findings to SQLite."""

    with sqlite3.connect(DB_PATH) as connection:
        results.to_sql(
            "validation_issues",
            connection,
            if_exists="replace",
            index=False
        )


def get_validation_results():
    """Retrieve stored validation findings."""

    with sqlite3.connect(DB_PATH) as connection:
        return pd.read_sql_query(
            "SELECT * FROM validation_issues",
            connection
        )


if __name__ == "__main__":
    from src.data_loader import load_equipment_data
    from src.validator import validate_equipment

    equipment = load_equipment_data()
    issues = validate_equipment(equipment)

    save_validation_results(issues)

    print("Validation results saved to SQLite.\n")

    stored_issues = get_validation_results()

    print(stored_issues.to_string(index=False))
    print(f"\nStored issues: {len(stored_issues)}")
