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
    cost_per_semester = annual_cost / SEMESTERS_PER_YEAR
    return cost_per_semester


def cost_per_month(annual_cost):
    cost_per_month = annual_cost / MONTHS_PER_YEAR
    return cost_per_month


def cost_per_day(annual_cost):
    cost_per_day = annual_cost / (CLASS_DAYS_PER_SEMESTER * SEMESTERS_PER_YEAR)
    return cost_per_day


def cost_per_credit(annual_cost, credits):
    cost_per_credit = (annual_cost / SEMESTERS_PER_YEAR) / credits
    return cost_per_credit


def cost_per_class(annual_cost, credits):
    cost_per_class = (cost_per_credit(annual_cost, credits) * CS1430_CREDITS / CS1430_MEETINGS_PER_SEMESTER)
    return cost_per_class


def is_it_worth_it(minutes_late, how_long_is_class):
    half_class_time = how_long_is_class / 2
    if minutes_late <= half_class_time:
        return True
    else:
        return False 


# ---- PROGRAM ----

def main():
    annual_cost = float(input("Enter the total cost for one year: "))
    credits = float(input("Enter the number of credits for this semester: "))


    while True:
        print("1. How much does a semster cost?")
        print("2. How much does a month cost?")
        print("3. How much does a class day cost?")
        print("4. How much does a credit cost?")
        print("5. How much does a CS 1430 class meeting cost?")
        print("6. How late are you to class and is it worth it to go?")
        print("Q. Quit")
        choice = input("Choose an option: ")
        if choice == "Q":
            break
        elif choice == "1":
            print(f"One semester costs: ${cost_per_semester(annual_cost):.2f}")
        elif choice == "2":
            print(f"One month costs: ${cost_per_month(annual_cost):.2f}")
        elif choice == "3":
            print(f"One class day costs: ${cost_per_day(annual_cost):.2f}")
        elif choice == "4":
            print(f"One credit costs: ${cost_per_credit(annual_cost, credits):.2f}")
        elif choice == "5":
            print(f"One CS 1430 class meeting costs: ${cost_per_class(annual_cost, credits):.2f}")
        elif choice == "6":
            minutes_late = int(input("Enter how many minutes late are you: "))
            how_long_is_class = int(input("Enter how long is the class in minutes: "))
            if is_it_worth_it(minutes_late, how_long_is_class) == True:
                print(f"It's worth it to go to class.")
            else:
                print(f"Don't go, there's only {int(how_long_is_class - minutes_late)} minutes left in class.")


if __name__ == "__main__":
    main()
