"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    return annual_cost / SEMESTERS_PER_YEAR


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost / MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    return annual_cost / (SEMESTERS_PER_YEAR * CLASS_DAYS_PER_SEMESTER)


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    return cost_per_semester(annual_cost) / credits


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    return cost_per_credit(annual_cost, credits) * CS1430_CREDITS / CS1430_MEETINGS_PER_SEMESTER

def cost_of_skipped_class(annual_cost,credits, skipped):
    """Return the cost represented by skipping CS 1430 class."""
    return cost_per_class(annual_cost, credits) * skipped

# ---- PROGRAM ----

def main():
    annual_cost = float(input("Enter the total cost for one year: "))
    credits = int(input("Enter the number of credits taken this semester: "))

    while True:
        # Show your menu here.
        print("\nThe cost of college")
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost per day")
        print("4. Cost per credit")
        print("5. Cost per class")
        print("6. Worth it?")
        print("Q. Quit")

        choice = input("Choose an option: ")

        if choice == "Q":
            break

        # Add a branch for each menu option here.
        elif choice == "1":
            semester = cost_per_semester(annual_cost)
            print(f"Cost per semester: ${semester:.2f}")
        elif choice == "2":
            month = cost_per_month(annual_cost)
            print(f"Cost per month: ${month:.2f}")
        elif choice == "3":
            day = cost_per_day(annual_cost)
            print(f"Cost per day: ${day:.2f}")
        elif choice == "4":
            credit = cost_per_credit(annual_cost, credits)
            print(f"Cost per credit: ${credit:.2f}")
        elif choice == "5":
            class_cost = cost_per_class(annual_cost, credits)
            print(f"Cost per class: ${class_cost:.2f}")
        elif choice == "6":
            skipped = int(input("How many CS 1430 classes did you miss? "))
            skipped_cost = cost_of_skipped_class(annual_cost, credits, skipped)
            print(f"The cost of skipped classes is: ${skipped_cost:.2f}")
        else:
            print("Invalid option, please enter 1-6 or Q to quit.")

# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
