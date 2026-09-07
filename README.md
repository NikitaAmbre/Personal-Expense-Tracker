# 💰 Personal Expense Tracker

A simple and user-friendly **Command-Line Personal Expense Tracker** developed using Python.

This application helps users record, manage, analyze, and visualize their daily expenses. It stores expense data in a CSV file and provides useful reports and charts for better understanding of spending habits.

---

## 📌 Project Overview

Managing daily expenses manually can make it difficult to understand where money is being spent.

The **Personal Expense Tracker** provides a simple solution where users can:

- Add and store expenses
- View all recorded expenses
- Search expenses
- Categorize expenses
- Save and load expense data using CSV
- Generate spending reports
- Track monthly budget
- Identify highest expenses
- View Top 3 highest expenses
- Analyze category-wise spending
- Visualize spending using charts

The project is completely **Python-based and command-line driven**.

---

## 🎯 Objectives

The main objectives of this project are:

1. To maintain daily expense records digitally.
2. To categorize expenses for better analysis.
3. To store expense data permanently using CSV.
4. To generate useful spending reports.
5. To provide graphical visualization of expenses.
6. To implement input validation and error handling.
7. To help users understand their spending patterns.

---

## ✨ Features

### 1. Add Expense

Users can add a new expense by entering:

- Amount
- Category
- Date

Available categories:

- Food
- Transport
- Entertainment
- Shopping
- Bills
- Health
- Education
- Other

---

### 2. View Expenses

Users can view all recorded expenses in a structured format.

The application displays:

- Expense number
- Amount
- Category
- Date

---

### 3. Search Expenses

Users can search and filter expenses based on:

- Category
- Date

This makes it easier to find specific transactions.

---

### 4. CSV Data Storage

Expense data is stored in a CSV file.

The application supports:

- Saving expenses to CSV
- Loading expenses from CSV

This allows expense records to remain available after restarting the application.

---

### 5. Expense Summary

The application provides a quick summary containing:

- Total spending
- Average expense
- Highest expense
- Monthly budget information
- Remaining or exceeded budget

---

### 6. Monthly Budget Tracking

Users can set a monthly budget and compare their spending against it.

The application shows whether the user:

- Has money remaining within the budget
- Has reached the budget
- Has exceeded the budget

---

### 7. Detailed Expense Report

The report provides useful spending analysis such as:

- Total spending
- Average expense
- Category-wise spending
- Category-wise percentage
- Monthly spending
- Highest expense
- Top 3 highest expenses
- Budget information

---

### 8. Data Visualization

The project uses **Matplotlib** to visualize expense data.

Available visualizations include:

#### 📊 Category-wise Bar Chart

Shows spending for each expense category.

#### 🥧 Category-wise Pie Chart

Shows the percentage distribution of expenses by category.

#### 📈 Monthly Spending Chart

Shows how spending changes month by month.

#### 📉 Weekly Spending Chart

Shows spending trends based on weeks.

Charts are automatically saved in the `charts/` folder.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Application development |
| CSV | Data storage |
| Matplotlib | Data visualization |
| Datetime | Date handling |
| Lists & Dictionaries | Data management |
| Exception Handling | Input validation and error handling |

---

## 📂 Project Structure

```text
Personal-Expense-Tracker/
│
├── main.py
├── expenses.csv
├── requirements.txt
├── README.md
│
└── charts/
    ├── category_bar_chart.png
    ├── category_pie_chart.png
    ├── monthly_spending_chart.png
    └── weekly_spending_chart.png