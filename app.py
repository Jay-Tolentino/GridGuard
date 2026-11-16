
import streamlit as st
import pandas as pd

from src.data_loader import load_equipment_data
from src.validator import validate_equipment
from src.database import save_validation_results
from src.reporting import generate_csv_report, generate_excel_report

st.set_page_config(
    page_title="GridGuard",
    page_icon="🛡️",
    layout="wide"
)

st.title("GridGuard")
st.subheader("Reliability Risk & Compliance Data Validator")

st.caption(
    "Independent educational prototype using synthetic utility data. "
    "Not affiliated with SMUD."
)

# Load and validate equipment records
equipment = load_equipment_data()
issues = validate_equipment(equipment)

# Save latest findings
save_validation_results(issues)

# Calculate summary metrics
total_assets = len(equipment)
total_issues = len(issues)
affected_assets = issues["asset_id"].nunique()

st.divider()

# Dashboard metrics
col1, col2, col3 = st.columns(3)

col1.metric("Total Equipment Records", total_assets)
col2.metric("Validation Issues", total_issues)
col3.metric("Affected Assets", affected_assets)

st.divider()

# Display detected problems
st.header("Validation Findings")

if issues.empty:
    st.success("No validation issues detected.")
else:
    st.warning(f"{total_issues} issue(s) require review.")
    st.dataframe(issues, use_container_width=True, hide_index=True)

# Issue breakdown
st.header("Issues by Category")

if not issues.empty:
    issue_counts = (
        issues["issue_type"]
        .value_counts()
        .rename_axis("Issue Type")
        .reset_index(name="Count")
    )

    st.bar_chart(
        issue_counts,
        x="Issue Type",
        y="Count"
    )

# Original dataset
st.header("Equipment Risk Records")

st.dataframe(
    equipment,
    use_container_width=True,
    hide_index=True
)

st.caption(
    "Risk scores use a demonstration formula: "
    "Likelihood × Impact. Not an official utility standard."
)

# Downloadable validation reports
st.divider()
st.header("Export Reports")

csv_report = generate_csv_report(issues)
excel_report = generate_excel_report(equipment, issues)

col_csv, col_excel = st.columns(2)

with col_csv:
    st.download_button(
        label="Download CSV Report",
        data=csv_report,
        file_name="gridguard_validation_report.csv",
        mime="text/csv"
    )

with col_excel:
    st.download_button(
        label="Download Excel Report",
        data=excel_report,
        file_name="gridguard_validation_report.xlsx",
        mime=(
            "application/vnd.openxmlformats-officedocument."
            "spreadsheetml.sheet"
        )
    )
