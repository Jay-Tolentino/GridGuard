
from io import BytesIO

import pandas as pd


def generate_csv_report(issues):
    """Generate a CSV report of validation findings."""
    return issues.to_csv(index=False).encode("utf-8")


def generate_excel_report(equipment, issues):
    """Generate an Excel workbook containing equipment and findings."""

    output = BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        issues.to_excel(
            writer,
            sheet_name="Validation Findings",
            index=False
        )

        equipment.to_excel(
            writer,
            sheet_name="Equipment Records",
            index=False
        )

    return output.getvalue()
