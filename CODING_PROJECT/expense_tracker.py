import math
from datetime import datetime

expenses = []

def add_expense():
    item = input("Enter Expense Name: ")
    amount = float(input("Enter Amount: "))
    date = datetime.now().strftime('%Y-%m-%d')
    expenses.append((item, amount, date))
    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("No expenses recorded.")
    else:
        for item in expenses:
            print(f"Item: {item[0]}, Amount: {item[1]}, Date: {item[2]}")

def monthly_expense():
    total = sum([item[1] for item in expenses])
    print(f"Total Monthly Expense: {total}")

def yearly_projection():
    monthly = sum([item[1] for item in expenses])
    yearly = math.ceil(monthly * 12)
    print(f"Estimated Yearly Expense: {yearly}")

def display_menu():
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Calculate Monthly and Yearly Expense")
    print("4. Exit")

def run_expense_tracker():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_expense()
            yearly_projection()
        elif choice == "4":
            print("Thank you for using the Expense Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

run_expense_tracker()
