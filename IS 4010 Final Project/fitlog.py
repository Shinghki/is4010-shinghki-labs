import argparse
from tracker import log_water, log_workout, get_summary, get_history

VALID_WORKOUTS = ["walking", "running", "tennis", "yoga", "pilates", "lifting"]


def interactive_menu():
    """Run an interactive menu for logging data."""
    print("\n🏋️  Welcome to FitLog!")

    while True:
        print("\nWhat would you like to do?")
        print("  1. Log water")
        print("  2. Log a workout")
        print("  3. View today's summary")
        print("  4. View all history")
        print("  5. Quit")

        choice = input("\nEnter 1, 2, 3, 4, or 5: ").strip()

        if choice == "1":
            ounces = input("How many ounces of water? ").strip()
            try:
                ounces = float(ounces)
                if ounces <= 0:
                    print("Please enter a positive number.")
                else:
                    log_water(ounces)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "2":
            print("\nWorkout types: walking, running, tennis, yoga, pilates, lifting")
            workout_type = input("What type of workout? ").strip().lower()

            if workout_type not in VALID_WORKOUTS:
                print(f"Unknown workout type '{workout_type}'.")
                continue

            minutes = input("How many minutes? ").strip()
            try:
                minutes = int(minutes)
                if minutes <= 0:
                    print("Please enter a positive number of minutes.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a whole number.")
                continue

            distance = None
            if workout_type in ["walking", "running"]:
                distance = input("How many miles? ").strip()
                try:
                    distance = float(distance)
                except ValueError:
                    print("Invalid distance. Logging without distance.")
                    distance = None

            log_workout(workout_type, minutes, distance)

        elif choice == "3":
            get_summary()

        elif choice == "4":
            get_history()

        elif choice == "5":
            print("Goodbye! Keep it up 💪")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")


def main():
    parser = argparse.ArgumentParser(
        prog="fitlog",
        description="A personal health tracker for workouts and water intake."
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # --- Water command ---
    water_parser = subparsers.add_parser("water", help="Log ounces of water")
    water_parser.add_argument("ounces", type=float, help="Ounces of water to log")

    # --- Workout command ---
    workout_parser = subparsers.add_parser("workout", help="Log a workout")
    workout_parser.add_argument(
        "type",
        choices=VALID_WORKOUTS,
        help="Type of workout"
    )
    workout_parser.add_argument("minutes", type=int, help="Minutes spent on workout")
    workout_parser.add_argument(
        "distance",
        type=float,
        nargs="?",
        default=None,
        help="Distance in miles (only for walking or running)"
    )

    # --- Summary command ---
    summary_parser = subparsers.add_parser("summary", help="View today's summary")
    summary_parser.add_argument(
        "--date",
        type=str,
        default=None,
        help="Date to view summary for (format: YYYY-MM-DD). Defaults to today."
    )

    args = parser.parse_args()

    if args.command == "water":
        if args.ounces <= 0:
            print("Please enter a positive number of ounces.")
        else:
            log_water(args.ounces)

    elif args.command == "workout":
        if args.minutes <= 0:
            print("Please enter a positive number of minutes.")
        else:
            log_workout(args.type, args.minutes, args.distance)

    elif args.command == "summary":
        get_summary(args.date)

    else:
        # No command given — launch interactive menu
        interactive_menu()


if __name__ == "__main__":
    main()