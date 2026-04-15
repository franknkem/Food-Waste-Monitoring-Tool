import csv
import argparse
from collections import Counter, defaultdict
from pathlib import Path

DATA_FILE = "data/food_waste.csv"
REPORT_FILE = "reports/waste_report.txt"


# ----------------------------
# LOAD DATA
# ----------------------------
def load_data(filename):
    records = []
    with open(filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert quantity to float
            row["quantity_wasted_kg"] = float(row["quantity_wasted_kg"])
            records.append(row)
    return records


# ----------------------------
# TOTAL WASTE
# ----------------------------
def total_waste(records):
    total = sum(r["quantity_wasted_kg"] for r in records)
    print(f"Total Food Waste: {total:.2f} kg")


# ----------------------------
# WASTE BY FOOD TYPE
# ----------------------------
def waste_by_food(records):
    food_totals = defaultdict(float)

    for r in records:
        food_totals[r["food_item"]] += r["quantity_wasted_kg"]

    print("Waste by Food Type")
    print("-------------------")
    for food, qty in food_totals.items():
        print(f"{food}: {qty:.2f} kg")


# ----------------------------
# WASTE BY MEAL TYPE
# ----------------------------
def waste_by_meal(records):
    meal_totals = defaultdict(float)

    for r in records:
        meal_totals[r["meal_type"]] += r["quantity_wasted_kg"]

    print("Waste by Meal Type")
    print("-------------------")
    for meal, qty in meal_totals.items():
        print(f"{meal}: {qty:.2f} kg")


# ----------------------------
# WASTE BY REASON
# ----------------------------
def waste_by_reason(records):
    reason_totals = defaultdict(float)

    for r in records:
        reason_totals[r["reason"]] += r["quantity_wasted_kg"]

    print("Waste by Reason")
    print("-------------------")
    for reason, qty in reason_totals.items():
        print(f"{reason}: {qty:.2f} kg")


# ----------------------------
# ADD NEW RECORD
# ----------------------------
def add_record():
    print("Add New Food Waste Record")
    print("--------------------------")

    date = input("Date (YYYY-MM-DD): ")
    meal = input("Meal Type (Breakfast/Lunch/Dinner): ")
    food = input("Food Item: ")
    qty = input("Quantity Wasted (kg): ")
    reason = input("Reason: ")
    notes = input("Notes: ")

    with open(DATA_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([date, meal, food, qty, reason, notes])

    print("Record added successfully.")


# ----------------------------
# GENERATE REPORT
# ----------------------------
def generate_report(records):
    from collections import defaultdict

    total = sum(r["quantity_wasted_kg"] for r in records)

    food_totals = defaultdict(float)
    reason_totals = defaultdict(float)

    for r in records:
        food_totals[r["food_item"]] += r["quantity_wasted_kg"]
        reason_totals[r["reason"]] += r["quantity_wasted_kg"]

    report_lines = [
        "Food Waste Monitoring Report",
        "============================",
        f"Total Waste: {total:.2f} kg",
        "",
        "Waste by Food Item:"
    ]

    for food, qty in food_totals.items():
        report_lines.append(f"- {food}: {qty:.2f} kg")

    report_lines.append("")
    report_lines.append("Waste by Reason:")

    for reason, qty in reason_totals.items():
        report_lines.append(f"- {reason}: {qty:.2f} kg")

    report_text = "\n".join(report_lines)

    print(report_text)

    Path("reports").mkdir(exist_ok=True)

    with open(REPORT_FILE, "w") as f:
        f.write(report_text)

    print(f"\nReport saved to {REPORT_FILE}")

# ----------------------------
# MAIN
# ----------------------------
def main():
    parser = argparse.ArgumentParser(description="Food Waste Monitoring Tool")

    parser.add_argument("--total", action="store_true")
    parser.add_argument("--by-food", action="store_true")
    parser.add_argument("--by-meal", action="store_true")
    parser.add_argument("--by-reason", action="store_true")
    parser.add_argument("--add", action="store_true")
    parser.add_argument("--report", action="store_true")

    args = parser.parse_args()

    if args.add:
        add_record()
        return

    records = load_data(DATA_FILE)

    if args.total:
        total_waste(records)
    elif args.by_food:
        waste_by_food(records)
    elif args.by_meal:
        waste_by_meal(records)
    elif args.by_reason:
        waste_by_reason(records)
    elif args.report:
        generate_report(records)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()