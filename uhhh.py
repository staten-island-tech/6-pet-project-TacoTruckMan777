import csv
import json
from pathlib import Path
from typing import Dict, Any, Tuple

def load_weapon_db(csv_path: Path) -> Dict[str, Dict[str, Any]]:
    """
    Load CSV into a dict keyed by lower-case weapon name -> full row dict.
    """
    csv_path = Path(csv_path)
    db: Dict[str, Dict[str, Any]] = {}
    with csv_path.open(newline='', encoding='utf-8') as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            name = (row.get("Name") or "").strip()
            if not name:
                continue
            db[name.lower()] = row
    return db

def load_inventory(inv_path: Path) -> Dict[str, int]:
    inv_path = Path(inv_path)
    if not inv_path.exists():
        return {}
    with inv_path.open('r', encoding='utf-8') as fh:
        return json.load(fh)

def save_inventory(inv_path: Path, inventory: Dict[str, int]) -> None:
    inv_path = Path(inv_path)
    inv_path.parent.mkdir(parents=True, exist_ok=True)
    with inv_path.open('w', encoding='utf-8') as fh:
        json.dump(inventory, fh, indent=2, ensure_ascii=False)

def add_weapon_to_inventory(weapon_name: str, qty: int, csv_path: Path, inv_path: Path) -> Tuple[bool, str]:
    """
    Add qty of weapon_name to the user's inventory.
    Returns (success, message).
    """
    db = load_weapon_db(csv_path)
    key = weapon_name.strip().lower()
    if key not in db:
        return False, f"Weapon not found in DB: {weapon_name}"
    inventory = load_inventory(inv_path)
    actual_name = db[key].get("Name", weapon_name)
    inventory[actual_name] = inventory.get(actual_name, 0) + int(qty)
    save_inventory(inv_path, inventory)
    return True, f"Added {qty} x {actual_name} to inventory."

# Example small helper to list weapon info
def get_weapon_info(weapon_name: str, csv_path: Path) -> Dict[str, Any] | None:
    db = load_weapon_db(csv_path)
    return db.get(weapon_name.strip().lower())











from pathlib import Path
from elden_weapon_db import add_weapon_to_inventory, get_weapon_info

CSV = Path(__file__).parent / "elden_ring_weapon.csv"
INVENTORY = Path(__file__).parent / "inventory.json"

def main():
    # quick manual example
    name = "Rivers of Blood"
    qty = 1

    info = get_weapon_info(name, CSV)
    if info:
        print("Weapon found:", info.get("Name"), "Type:", info.get("Type"))
    ok, msg = add_weapon_to_inventory(name, qty, CSV, INVENTORY)
    print(msg)

if __name__ == "__main__":
    main()