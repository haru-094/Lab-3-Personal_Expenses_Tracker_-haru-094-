Personal Expenses Tracker
Project Overview

This project is a command-line Personal Finance Tracker application built using vanilla Python. It allows users to manage daily expenses, track their remaining balance, and generate expense reports. Additionally, a companion Shell script (archive_expenses.sh) is provided to handle file organization, archiving, and automated searching of past records.

File Structure

The repository consists of the following required files:

expenses-tracker.py: The main Python application logic.

archive_expenses.sh: The shell script for archiving and searching.

balance.txt: A text file storing the current numerical balance.

Part 1: Python Application (expenses-tracker.py)

The Python application serves as the main interface for the user. It includes a loop-based menu system with the following features:

Features

Check Remaining Balance:

Reads the current funds from balance.txt.

Calculates total expenses and displays the Available Balance.

Allows the user to add funds (deposit), which updates the balance.txt file.

View Expenses:

Provides a sub-menu for searching specific transactions.

Search by Item: Find expenses by the name of the item purchased.

Search by Amount: Find expenses that match a specific cost.

Add New Expense:

Displays the current available balance before input.

Prompts for a Date (YYYY-MM-DD), Item Name, and Amount.

Validation: Prevents the user from spending more than their available balance.

Storage: Saves validated expenses into a file named expenses_YYYY-MM-DD.txt.

Updates the main balance automatically upon success.

Exit:

Gracefully terminates the program.

Part 2: Shell Script (archive_expenses.sh)

The shell script handles system automation and file management.

Features

Directory Management: Automatically checks for an archives directory and creates it if it does not exist.

Archiving: Moves daily expense files (expenses_*.txt) from the root directory to the archives folder.

Logging: Records every archival operation with a timestamp in archive_log.txt.

Search Capability: Enables the user to search the archives directory for a specific date (e.g., 2024-11-07) and display the content of that file in the terminal.

Setup & Usage Instructions

Prerequisites

Python 3.x installed.

A Bash terminal (Linux, macOS, Git Bash on Windows).

1. Initial Configuration

Ensure you have a balance.txt file in the same directory as the script. It should contain a single starting number (e.g., 50000).

echo "50000" > balance.txt

2. Running the Python Tracker

To start the application, run:

python3 expenses-tracker.py

Follow the on-screen menu prompts to add expenses or check your balance.

3. Running the Shell Script

First, ensure the script has execution permissions:

chmod +x archive_expenses.sh

To Archive Files:
Run the script without arguments to move current expense files to the archive folder:

./archive_expenses.sh

To Search Archives:
(Depending on your specific implementation, you might run it interactively or pass the data. Example below assumes interactive or argument-based):

./archive_expenses.sh
# Follow prompts to enter a date (e.g., 2024-11-07) to view that specific file.
