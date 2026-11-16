from pathlib import Path
import pandas as pd


DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "equipment_risk.csv"


def load_equipment_data():
    """Load synthetic electrical equipment records from CSV."""
    return pd.read_csv(DATA_PATH)


if __name__ == "__main__":
    equipment = load_equipment_data()

    print("GridGuard - Equipment Risk Dataset")
    print(equipment.to_string(index=False))

    print(f"\nTotal equipment records: {len(equipment)}")