import pandas as pd

from src.data_loader import load_equipment_data


def validate_equipment(df):
    """Validate equipment risk assessment records."""

    issues = []

    for _, row in df.iterrows():
        asset_id = row["asset_id"]
        likelihood = row["likelihood"]
        impact = row["impact"]
        risk_score = row["risk_score"]

        # Check that likelihood and impact are valid integers (1-5)
        for field, value in [
            ("likelihood", likelihood),
            ("impact", impact),
        ]:
            if (
                pd.isna(value)
                or not isinstance(value, (int, float))
                or not 1 <= value <= 5
                or value % 1 != 0
            ):
                issues.append({
                    "asset_id": asset_id,
                    "issue_type": "Invalid Risk Input",
                    "description": f"{field} must be an integer from 1 to 5",
                })

        # Do not calculate risk when inputs are invalid
        if not all(
            pd.notna(value)
            and isinstance(value, (int, float))
            and 1 <= value <= 5
            and value % 1 == 0
            for value in [likelihood, impact]
        ):
            continue

        expected_score = int(likelihood * impact)

        if pd.isna(risk_score):
            issues.append({
                "asset_id": asset_id,
                "issue_type": "Missing Risk Score",
                "description": f"Expected risk score: {expected_score}",
            })

        elif risk_score != expected_score:
            issues.append({
                "asset_id": asset_id,
                "issue_type": "Risk Score Mismatch",
                "description": (
                    f"Recorded: {risk_score}, "
                    f"Expected: {expected_score}"
                ),
            })

    return pd.DataFrame(
        issues,
        columns=["asset_id", "issue_type", "description"],
    )


if __name__ == "__main__":
    equipment = load_equipment_data()
    results = validate_equipment(equipment)

    print("\nGridGuard - Risk Validation Report")
    print("----------------------------------")

    if results.empty:
        print("No validation issues found.")
    else:
        print(results.to_string(index=False))

    print(f"\nTotal issues detected: {len(results)}")