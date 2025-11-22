Personal Expenses Tracker
📌 Project Overview
This project is a command-line Personal Finance Tracker built using vanilla Python. It allows users to:

Manage daily expenses

Track remaining balance

Generate expense reports

Additionally, a companion Shell script (archive_expenses.sh) is provided to handle file organization, archiving, and automated searching of past records.

📂 File Structure
expenses-tracker.py → Main Python application logic

archive_expenses.sh → Shell script for archiving and searching

balance.txt → Stores the current numerical balance

🖥️ Part 1: Python Application (expenses-tracker.py)
Features
Check Remaining Balance

Reads current funds from balance.txt

Calculates total expenses and displays available balance

Allows deposits (updates balance.txt)

View Expenses

Search transactions by Item or Amount

Add New Expense

Displays current balance before input

Prompts for Date (YYYY-MM-DD), Item Name, and Amount

Validates against available balance

Saves expenses into expenses_YYYY-MM-DD.txt

Updates balance automatically

Exit

Gracefully terminates the program

🛠️ Part 2: Shell Script (archive_expenses.sh)
Features
Directory Management → Creates archives/ folder if missing

Archiving → Moves daily expense files (expenses_*.txt) into archives/

Logging → Records archival operations with timestamps in archive_log.txt

Search Capability → Search archives by date (e.g., 2024-11-07) and display file contents

⚙️ Setup & Usage Instructions
Prerequisites
Python 3.x installed

Bash terminal (Linux, macOS, or Git Bash on Windows)

1. Initial Configuration
Create a starting balance file:

bash
echo "50000" > balance.txt
2. Running the Python Tracker
bash
python3 expenses-tracker.py
Follow the on-screen menu prompts to add expenses or check your balance.

3. Running the Shell Script
Grant execution permissions:

bash
chmod +x archive_expenses.sh
To Archive Files:

bash
./archive_expenses.sh
To Search Archives:

bash
./archive_expenses.sh
# Enter a date (e.g., 2024-11-07) when prompted
