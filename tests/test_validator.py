import pandas as pd

from src.validator import validate_equipment


def make_record(likelihood=3, impact=4, risk_score=12):
    """Create a sample equipment record for testing."""
    return pd.DataFrame([{
        "asset_id": "TEST-001",
        "likelihood": likelihood,
        "impact": impact,
        "risk_score": risk_score
    }])


def test_valid_risk_score():
    df = make_record(3, 4, 12)
    issues = validate_equipment(df)

    assert issues.empty


def test_incorrect_risk_score():
    df = make_record(3, 4, 9)
    issues = validate_equipment(df)

    assert len(issues) == 1
    assert issues.iloc[0]["issue_type"] == "Risk Score Mismatch"


def test_missing_risk_score():
    df = make_record(3, 5, None)
    issues = validate_equipment(df)

    assert len(issues) == 1
    assert issues.iloc[0]["issue_type"] == "Missing Risk Score"


def test_invalid_likelihood():
    df = make_record(6, 3, 18)
    issues = validate_equipment(df)

    assert len(issues) == 1
    assert issues.iloc[0]["issue_type"] == "Invalid Risk Input"


def test_missing_likelihood():
    df = make_record(None, 3, 9)
    issues = validate_equipment(df)

    assert len(issues) == 1
    assert issues.iloc[0]["issue_type"] == "Invalid Risk Input"



def test_all_valid_records():
    df = pd.concat([
        make_record(2, 3, 6),
        make_record(4, 5, 20),
        make_record(1, 2, 2)
    ], ignore_index=True)

    # Each equipment record must have a unique asset ID
    df["asset_id"] = ["TEST-001", "TEST-002", "TEST-003"]

    issues = validate_equipment(df)

    assert issues.empty


def test_duplicate_asset_ids():
    df = pd.concat([
        make_record(2, 3, 6),
        make_record(4, 5, 20)
    ], ignore_index=True)

    issues = validate_equipment(df)

    assert len(issues) == 1
    assert issues.iloc[0]["issue_type"] == "Duplicate Asset ID"


def test_unique_asset_ids():
    df = pd.concat([
        make_record(2, 3, 6),
        make_record(4, 5, 20)
    ], ignore_index=True)

    df["asset_id"] = ["TEST-001", "TEST-002"]

    issues = validate_equipment(df)

    assert issues.empty


def test_future_inspection_date():
    df = make_record(3, 4, 12)
    df["last_inspection"] = "2099-01-01"

    issues = validate_equipment(df)

    assert len(issues) == 1
    assert issues.iloc[0]["issue_type"] == "Future Inspection Date"


def test_invalid_inspection_date():
    df = make_record(3, 4, 12)
    df["last_inspection"] = "not-a-real-date"

    issues = validate_equipment(df)

    assert len(issues) == 1
    assert issues.iloc[0]["issue_type"] == "Invalid Inspection Date"
