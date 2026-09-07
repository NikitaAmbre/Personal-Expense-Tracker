import csv
import matplotlib.pyplot as plt
import os
from datetime import datetime

expenses = []

# ---------------- COMMON EXPENSE CATEGORIES ----------------

CATEGORIES = [
    "Food",
    "Transport",
    "Entertainment",
    "Shopping",
    "Bills",
    "Health",
    "Education",
    "Other"
]

# ---------------- MONTHLY BUDGET ----------------

monthly_budget = 0


# ---------------- ADD EXPENSE ----------------

def add_expense():

    print("\n--- Add Expense ---")

    # Amount validation
    while True:

        try:

            amount = float(
                input("Enter expense amount: ₹")
            )

            if amount <= 0:
                print("Amount must be greater than 0.")

            else:
                break

        except ValueError:

            print(
                "Invalid amount! Please enter a number."
            )

    # Category selection
    print("\n--- Select Category ---")

    for number, category in enumerate(
        CATEGORIES,
        start=1
    ):

        print(
            f"{number}. {category}"
        )

    while True:

        try:

            category_choice = int(
                input("Enter category number: ")
            )

            if 1 <= category_choice <= len(CATEGORIES):

                category = CATEGORIES[
                    category_choice - 1
                ]

                break

            else:

                print(
                    "Please select a number between 1 and 8."
                )

        except ValueError:

            print(
                "Invalid choice! Please enter a number."
            )

    # Date validation
    while True:

        date = input(
            "Enter expense date (YYYY-MM-DD): "
        ).strip()

        try:

            datetime.strptime(
                date,
                "%Y-%m-%d"
            )

            break

        except ValueError:

            print(
                "Invalid date! Please use YYYY-MM-DD format."
            )

    # Create expense
    expense = {
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)

    print(
        "\nExpense added successfully!"
    )


# ---------------- VIEW EXPENSES ----------------

def view_expenses():

    print("\n" + "=" * 65)
    print("                        ALL EXPENSES")
    print("=" * 65)

    if len(expenses) == 0:

        print("No expenses found.")
        print("=" * 65)

        return

    print(
        f"{'No.':<8}"
        f"{'Amount':<18}"
        f"{'Category':<22}"
        f"{'Date':<15}"
    )

    print("-" * 65)

    for number, expense in enumerate(
        expenses,
        start=1
    ):

        print(
            f"{number:<8}"
            f"₹{expense['amount']:<17.2f}"
            f"{expense['category']:<22}"
            f"{expense['date']:<15}"
        )

    total_spending = sum(
        expense["amount"]
        for expense in expenses
    )

    print("-" * 65)

    print(
        f"Total Expenses: {len(expenses)}"
    )

    print(
        f"Total Spending: ₹{total_spending:.2f}"
    )

    print("=" * 65)


# ---------------- SEARCH EXPENSES ----------------

def search_expenses():

    if len(expenses) == 0:

        print(
            "\nNo expenses available to search."
        )

        return

    while True:

        print("\n--- Search Expenses ---")

        print("1. Search by Category")
        print("2. Search by Date")
        print("3. Back to Main Menu")

        choice = input(
            "Enter your choice: "
        ).strip()

        # Search by Category
        if choice == "1":

            print("\n--- Select Category ---")

            for number, category in enumerate(
                CATEGORIES,
                start=1
            ):

                print(
                    f"{number}. {category}"
                )

            while True:

                try:

                    category_choice = int(
                        input(
                            "Enter category number: "
                        )
                    )

                    if 1 <= category_choice <= len(CATEGORIES):

                        selected_category = CATEGORIES[
                            category_choice - 1
                        ]

                        break

                    else:

                        print(
                            "Please select a number between 1 and 8."
                        )

                except ValueError:

                    print(
                        "Invalid choice! Please enter a number."
                    )

            found = False

            print(
                f"\n--- {selected_category} Expenses ---"
            )

            for number, expense in enumerate(
                expenses,
                start=1
            ):

                if expense["category"] == selected_category:

                    print(
                        f"{number:<8}"
                        f"₹{expense['amount']:<17.2f}"
                        f"{expense['category']:<22}"
                        f"{expense['date']:<15}"
                    )

                    found = True

            if not found:

                print(
                    "No expenses found in this category."
                )

        # Search by Date
        elif choice == "2":

            while True:

                search_date = input(
                    "Enter date to search (YYYY-MM-DD): "
                ).strip()

                try:

                    datetime.strptime(
                        search_date,
                        "%Y-%m-%d"
                    )

                    break

                except ValueError:

                    print(
                        "Invalid date! Please use "
                        "YYYY-MM-DD format."
                    )

            found = False

            print(
                f"\n--- Expenses on {search_date} ---"
            )

            for number, expense in enumerate(
                expenses,
                start=1
            ):

                if expense["date"] == search_date:

                    print(
                        f"{number:<8}"
                        f"₹{expense['amount']:<17.2f}"
                        f"{expense['category']:<22}"
                        f"{expense['date']:<15}"
                    )

                    found = True

            if not found:

                print(
                    "No expenses found for this date."
                )

        # Back to Main Menu
        elif choice == "3":

            break

        else:

            print(
                "Invalid choice! Please select 1, 2 or 3."
            )


# ---------------- SAVE EXPENSES ----------------

def save_expenses():

    with open(
        "expenses.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "amount",
                "category",
                "date"
            ]
        )

        writer.writeheader()
        writer.writerows(expenses)

    print(
        "\nExpenses saved successfully!"
    )


# ---------------- LOAD EXPENSES ----------------

def load_expenses():

    try:

        with open(
            "expenses.csv",
            "r"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                expense = {
                    "amount": float(
                        row["amount"]
                    ),
                    "category": row["category"],
                    "date": row["date"]
                }

                expenses.append(expense)

        print(
            "Previous expenses loaded successfully!"
        )

    except FileNotFoundError:

        print(
            "No previous expense file found. "
            "Starting with an empty list."
        )


# ---------------- EXPENSE SUMMARY ----------------

def show_summary():

    print("\n" + "=" * 65)
    print("                  EXPENSE SUMMARY")
    print("=" * 65)

    if len(expenses) == 0:

        print("No expenses available.")
        print("=" * 65)

        return

    total_spending = sum(
        expense["amount"]
        for expense in expenses
    )

    highest_expense = max(
        expenses,
        key=lambda expense: expense["amount"]
    )

    average_spending = (
        total_spending / len(expenses)
    )

    print(
        f"Total Expenses      : {len(expenses)}"
    )

    print(
        f"Total Spending      : ₹{total_spending:.2f}"
    )

    print(
        f"Average Expense     : ₹{average_spending:.2f}"
    )

    print(
        f"Highest Expense     : "
        f"₹{highest_expense['amount']:.2f}"
    )

    print(
        f"Highest Category    : "
        f"{highest_expense['category']}"
    )

    print(
        f"Highest Expense Date: "
        f"{highest_expense['date']}"
    )

    # Budget information
    if monthly_budget > 0:

        print(
            f"Monthly Budget      : "
            f"₹{monthly_budget:.2f}"
        )

        remaining_budget = (
            monthly_budget - total_spending
        )

        if remaining_budget >= 0:

            print(
                f"Remaining Budget    : "
                f"₹{remaining_budget:.2f}"
            )

        else:

            print(
                f"Budget Exceeded     : "
                f"₹{abs(remaining_budget):.2f}"
            )

            print(
                "⚠ Warning: Monthly budget exceeded!"
            )

    else:

        print(
            "Monthly Budget      : Not Set"
        )

    print("=" * 65)


# ---------------- SET MONTHLY BUDGET ----------------

def set_monthly_budget():

    global monthly_budget

    print("\n" + "=" * 65)
    print("                    SET MONTHLY BUDGET")
    print("=" * 65)

    while True:

        try:

            budget = float(
                input(
                    "Enter your monthly budget: ₹"
                )
            )

            if budget <= 0:

                print(
                    "Budget must be greater than 0."
                )

            else:

                monthly_budget = budget

                print(
                    f"\nMonthly budget set successfully: "
                    f"₹{monthly_budget:.2f}"
                )

                break

        except ValueError:

            print(
                "Invalid budget! Please enter a number."
            )


# ---------------- GENERATE REPORT ----------------

def generate_report():

    if len(expenses) == 0:

        print(
            "\nNo expenses available to generate report."
        )

        return

    print("\n" + "=" * 65)
    print("                     EXPENSE REPORT")
    print("=" * 65)

    # Total spending
    total_spending = sum(
        expense["amount"]
        for expense in expenses
    )

    print(
        f"\nTotal Spending      : "
        f"₹{total_spending:.2f}"
    )

    # Average expense
    average_expense = (
        total_spending / len(expenses)
    )

    print(
        f"Average Expense     : "
        f"₹{average_expense:.2f}"
    )

    # Category-wise spending
    category_spending = {}

    for expense in expenses:

        category = expense["category"]
        amount = expense["amount"]

        if category in category_spending:

            category_spending[category] += amount

        else:

            category_spending[category] = amount

    print(
        "\n--- Category-wise Spending ---"
    )

    print("-" * 65)

    print(
        f"{'Category':<22}"
        f"{'Amount':<18}"
        f"{'Percentage':<15}"
    )

    print("-" * 65)

    for category, amount in category_spending.items():

        percentage = (
            amount / total_spending
        ) * 100

        print(
            f"{category:<22}"
            f"₹{amount:<17.2f}"
            f"{percentage:.2f}%"
        )

    print("-" * 65)

    # Monthly spending
    monthly_spending = {}

    for expense in expenses:

        month = expense["date"][:7]
        amount = expense["amount"]

        if month in monthly_spending:

            monthly_spending[month] += amount

        else:

            monthly_spending[month] = amount

    print(
        "\n--- Monthly Spending ---"
    )

    print("-" * 40)

    for month, amount in sorted(
        monthly_spending.items()
    ):

        print(
            f"{month:<15} : ₹{amount:.2f}"
        )

    print("-" * 40)

    # Top 3 highest expenses
    top_expenses = sorted(
        expenses,
        key=lambda expense: expense["amount"],
        reverse=True
    )[:3]

    print(
        "\n--- Top 3 Highest Expenses ---"
    )

    print("-" * 65)

    print(
        f"{'Rank':<8}"
        f"{'Amount':<18}"
        f"{'Category':<22}"
        f"{'Date':<15}"
    )

    print("-" * 65)

    for rank, expense in enumerate(
        top_expenses,
        start=1
    ):

        print(
            f"{rank:<8}"
            f"₹{expense['amount']:<17.2f}"
            f"{expense['category']:<22}"
            f"{expense['date']:<15}"
        )

    print("-" * 65)

    # Highest expense
    highest_expense = max(
        expenses,
        key=lambda expense: expense["amount"]
    )

    print(
        "\n--- Highest Expense ---"
    )

    print(
        f"Amount   : "
        f"₹{highest_expense['amount']:.2f}"
    )

    print(
        f"Category : "
        f"{highest_expense['category']}"
    )

    print(
        f"Date     : "
        f"{highest_expense['date']}"
    )

    # Budget information in report
    if monthly_budget > 0:

        print(
            "\n--- Monthly Budget ---"
        )

        print(
            f"Budget          : "
            f"₹{monthly_budget:.2f}"
        )

        remaining_budget = (
            monthly_budget - total_spending
        )

        if remaining_budget >= 0:

            print(
                f"Remaining       : "
                f"₹{remaining_budget:.2f}"
            )

        else:

            print(
                f"Budget Exceeded : "
                f"₹{abs(remaining_budget):.2f}"
            )

    print("=" * 65)


# ---------------- VISUALIZATION ----------------

def show_visualization():

    if len(expenses) == 0:

        print(
            "\nNo expenses available for visualization."
        )

        return

    # Create charts folder
    os.makedirs(
        "charts",
        exist_ok=True
    )

    # Prepare category-wise data
    category_spending = {}

    for expense in expenses:

        category = expense["category"]
        amount = expense["amount"]

        if category in category_spending:

            category_spending[category] += amount

        else:

            category_spending[category] = amount

    categories = list(
        category_spending.keys()
    )

    amounts = list(
        category_spending.values()
    )

    # Visualization Menu Loop
    while True:

        print("\n" + "=" * 65)
        print("                  EXPENSE VISUALIZATION")
        print("=" * 65)

        print(
            "\n1. Category-wise Bar Chart"
        )

        print(
            "2. Category-wise Pie Chart"
        )

        print(
            "3. Monthly Spending Chart"
        )

        print(
            "4. Weekly Spending Chart"
        )

        print(
            "5. Back"
        )

        choice = input(
            "\nEnter your choice: "
        ).strip()

        # Category Bar Chart
        if choice == "1":

            plt.figure(
                figsize=(9, 5)
            )

            bars = plt.bar(
                categories,
                amounts
            )

            plt.title(
                "Category-wise Expense Spending",
                fontsize=15,
                fontweight="bold"
            )

            plt.xlabel(
                "Category"
            )

            plt.ylabel(
                "Amount (₹)"
            )

            plt.xticks(
                rotation=30
            )

            # Display values on bars
            for bar, amount in zip(
                bars,
                amounts
            ):

                plt.text(
                    bar.get_x()
                    + bar.get_width() / 2,
                    bar.get_height(),
                    f"₹{amount:.0f}",
                    ha="center",
                    va="bottom",
                    fontsize=9
                )

            plt.tight_layout()

            plt.savefig(
                "charts/category_bar_chart.png",
                dpi=300,
                bbox_inches="tight"
            )

            plt.show()

            print(
                "\nCategory bar chart saved successfully!"
            )

        # Category Pie Chart
        elif choice == "2":

            plt.figure(
                figsize=(8, 8)
            )

            plt.pie(
                amounts,
                labels=categories,
                autopct="%1.1f%%",
                startangle=90
            )

            plt.title(
                "Category-wise Expense Distribution",
                fontsize=15,
                fontweight="bold"
            )

            plt.tight_layout()

            plt.savefig(
                "charts/category_pie_chart.png",
                dpi=300,
                bbox_inches="tight"
            )

            plt.show()

            print(
                "\nCategory pie chart saved successfully!"
            )

        # Monthly Spending Chart
        elif choice == "3":

            monthly_spending = {}

            for expense in expenses:

                month = expense["date"][:7]
                amount = expense["amount"]

                if month in monthly_spending:

                    monthly_spending[month] += amount

                else:

                    monthly_spending[month] = amount

            months = sorted(
                monthly_spending.keys()
            )

            monthly_amounts = [
                monthly_spending[month]
                for month in months
            ]

            plt.figure(
                figsize=(9, 5)
            )

            plt.plot(
                months,
                monthly_amounts,
                marker="o",
                linewidth=2
            )

            plt.title(
                "Monthly Spending Trend",
                fontsize=15,
                fontweight="bold"
            )

            plt.xlabel(
                "Month"
            )

            plt.ylabel(
                "Amount (₹)"
            )

            plt.xticks(
                rotation=30
            )

            # Display values
            for month, amount in zip(
                months,
                monthly_amounts
            ):

                plt.text(
                    month,
                    amount,
                    f"₹{amount:.0f}",
                    ha="center",
                    va="bottom",
                    fontsize=9
                )

            plt.tight_layout()

            plt.savefig(
                "charts/monthly_spending_chart.png",
                dpi=300,
                bbox_inches="tight"
            )

            plt.show()

            print(
                "\nMonthly spending chart saved successfully!"
            )

        # Weekly Spending Chart
        elif choice == "4":

            weekly_spending = {}

            for expense in expenses:

                expense_date = datetime.strptime(
                    expense["date"],
                    "%Y-%m-%d"
                )

                year, week, _ = (
                    expense_date.isocalendar()
                )

                week_key = (
                    f"{year}-W{week:02d}"
                )

                amount = expense["amount"]

                if week_key in weekly_spending:

                    weekly_spending[week_key] += amount

                else:

                    weekly_spending[week_key] = amount

            weeks = sorted(
                weekly_spending.keys()
            )

            weekly_amounts = [
                weekly_spending[week]
                for week in weeks
            ]

            plt.figure(
                figsize=(10, 5)
            )

            plt.plot(
                weeks,
                weekly_amounts,
                marker="o",
                linewidth=2
            )

            plt.title(
                "Weekly Spending Trend",
                fontsize=15,
                fontweight="bold"
            )

            plt.xlabel(
                "Week"
            )

            plt.ylabel(
                "Amount (₹)"
            )

            plt.xticks(
                rotation=45
            )

            # Display values
            for week, amount in zip(
                weeks,
                weekly_amounts
            ):

                plt.text(
                    week,
                    amount,
                    f"₹{amount:.0f}",
                    ha="center",
                    va="bottom",
                    fontsize=8
                )

            plt.tight_layout()

            plt.savefig(
                "charts/weekly_spending_chart.png",
                dpi=300,
                bbox_inches="tight"
            )

            plt.show()

            print(
                "\nWeekly spending chart saved successfully!"
            )

        # Back to Main Menu
        elif choice == "5":

            print(
                "\nReturning to Main Menu..."
            )

            break

        else:

            print(
                "\nInvalid choice. "
                "Please enter a number from 1 to 5."
            )


# ---------------- MAIN MENU ----------------

def main():

    load_expenses()

    while True:

        print("\n" + "=" * 40)
        print("       PERSONAL EXPENSE TRACKER")
        print("=" * 40)

        print("1. Add an Expense")
        print("2. View All Expenses")
        print("3. Search Expenses")
        print("4. Expense Summary")
        print("5. Generate Report")
        print("6. Show Visualization")
        print("7. Set Monthly Budget")
        print("8. Save and Exit")

        choice = input(
            "\nEnter your choice: "
        ).strip()

        if choice == "1":

            add_expense()

        elif choice == "2":

            view_expenses()

        elif choice == "3":

            search_expenses()

        elif choice == "4":

            show_summary()

        elif choice == "5":

            generate_report()

        elif choice == "6":

            show_visualization()

        elif choice == "7":

            set_monthly_budget()

        elif choice == "8":

            save_expenses()

            print(
                "\nThank you for using "
                "Personal Expense Tracker!"
            )

            break

        else:

            print(
                "\nInvalid choice! "
                "Please select a number between 1 and 8."
            )


# ---------------- START PROGRAM ----------------

if __name__ == "__main__":

    main()