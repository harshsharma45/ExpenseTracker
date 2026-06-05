# ExpenseTracker
```markdown
# Python CLI Expense Tracker: Financial Dashboard

## 📖 Overview
This project is a Command-Line Interface (CLI) Expense Tracker built in Python. Designed as a real-time financial dashboard, it allows users to continuously log, remove, and view their daily expenses. 

This project was developed as **Project 2: The Expense Tracker** for the **DecodeLabs Industrial Training Kit (Batch 2026)**. It focuses heavily on data accumulation, mathematical logic, and preserving state within a continuous execution loop.

---

## ✨ Key Features
* **Data Accumulation:** Continuously calculates and manages the total financial state in real-time as users add or remove expenses.
* **Batch Data Entry:** Users can input multiple expenses sequentially in a single operation using dynamic looping.
* **Defensive Coding (Digital Poka-Yoke):** Implements strict `try-except` blocks to prevent application crashes when users accidentally input strings instead of numeric values.
* **Safe Deletion:** Validates the existence of specific financial data before attempting to remove it from the array, recalculating the live total instantly.
* **Graceful Shutdown (Kill Switch):** Captures and displays the final financial state before safely terminating the continuous application loop.

---

## 🛠️ Technical Architecture
* **State Preservation:** The application initializes critical variables (arrays and floats) outside the continuous loop to prevent "amnesia" and ensure data persists throughout the user session.
* **Data Transformation:** Converts raw string inputs into actionable floating-point numbers (`float()`) to accurately process currency calculations (e.g., $10.50).
* **The IPO Model:** Adheres to strict Input (Raw Data), Process (Validation & Computation), and Output (Refined Display) pathways without relying on external databases.

---

## 🚀 Getting Started

### Prerequisites
* **Python 3.x** must be installed on your system. No external dependencies are required.

### Installation & Execution
1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/harshsharma45/ExpenseTracker.git](https://github.com/harshsharma45/ExpenseTracker.git)

```

2. Open your terminal or command prompt.
3. Navigate to the project directory:
```bash
cd ExpenseTracker

```


4. Run the application:
```bash
python main.py

```


*(Note: Replace `main.py` with the actual name of your Python file if it is different).*

---

## 💻 Usage Guide

Upon running the script, you will see the main menu:

```text
Expense Tracker Using Python
Welcome to the Expense Tracker
Enter your choice:
1.Add Expenses
2.Remove Expenses
3.Total Expenses
4.Quit

```

* **Select `1**` to specify how many expenses you want to add, and then type the amounts sequentially.
* **Select `2**` to type the exact amount of an expense you wish to delete. The system will safely remove it and recalculate the total.
* **Select `3**` to see your current total spent and the number of transactions.
* **Select `4**` to display the final total and exit the application gracefully.

```

```
