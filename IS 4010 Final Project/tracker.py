import json
import os
from datetime import date

DATA_FILE = "data.json"


def load_data():
    """Load all logged data from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    """Save all data to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


def get_today():
    """Return today's date as a string like '2026-04-26'."""
    return str(date.today())


def log_water(ounces):
    """Add ounces of water to today's log."""
    data = load_data()
    today = get_today()

    if today not in data:
        data[today] = {"water": 0, "workouts": []}

    data[today]["water"] += ounces
    save_data(data)
    print(f"Logged {ounces} oz of water. Total today: {data[today]['water']} oz")


def log_workout(workout_type, minutes, distance=None):
    """Add a workout to today's log."""
    valid_types = ["walking", "running", "tennis", "yoga", "pilates", "lifting"]

    if workout_type not in valid_types:
        print(f"Unknown workout type '{workout_type}'. Choose from: {', '.join(valid_types)}")
        return

    data = load_data()
    today = get_today()

    if today not in data:
        data[today] = {"water": 0, "workouts": []}

    workout = {"type": workout_type, "minutes": minutes}

    if workout_type in ["walking", "running"] and distance is not None:
        workout["distance"] = distance

    data[today]["workouts"].append(workout)
    save_data(data)

    if distance:
        print(f"Logged {workout_type} for {minutes} min, {distance} miles.")
    else:
        print(f"Logged {workout_type} for {minutes} min.")


def get_summary(day=None):
    """Print a summary for a given day (defaults to today)."""
    data = load_data()

    if day is None:
        day = get_today()

    if day not in data:
        print(f"No data found for {day}.")
        return

    entry = data[day]
    water = entry.get("water", 0)
    workouts = entry.get("workouts", [])
    total_minutes = sum(w["minutes"] for w in workouts)

    print(f"\n=== Summary for {day} ===")
    print(f"💧 Water:    {water} oz")
    print(f"🏃 Workouts: {len(workouts)} session(s), {total_minutes} min total")

    for w in workouts:
        if "distance" in w:
            print(f"   - {w['type'].capitalize():<10} {w['minutes']} min, {w['distance']} miles")
        else:
            print(f"   - {w['type'].capitalize():<10} {w['minutes']} min")

def get_history():
    """Print a summary for all logged days."""
    data = load_data()

    if not data:
        print("No history found.")
        return

    print("\n=== Your FitLog History ===")
    for day in sorted(data.keys(), reverse=True):
        entry = data[day]
        water = entry.get("water", 0)
        workouts = entry.get("workouts", [])
        total_minutes = sum(w["minutes"] for w in workouts)

        print(f"\n📅 {day}")
        print(f"   💧 Water:    {water} oz")
        print(f"   🏃 Workouts: {len(workouts)} session(s), {total_minutes} min total")
        for w in workouts:
            if "distance" in w:
                print(f"      - {w['type'].capitalize():<10} {w['minutes']} min, {w['distance']} miles")
            else:
                print(f"      - {w['type'].capitalize():<10} {w['minutes']} min")