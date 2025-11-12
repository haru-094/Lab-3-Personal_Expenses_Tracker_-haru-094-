import os
import sys
from datetime import datetime


# Get the balance file path
balance_file_path = 'balance.txt'

# function to read the balance from balance file


def read_file():
    total = 0
    try:
        with open(balance_file_path, 'r') as f:
            total = f.read().strip()
            return float(total)
    except IOError:
        print("Error, can't read the balance file")
        sys.exit(1)


def update_balance(new_balance):

    try:
        with open(balance_file_path, 'w') as f:
            f.write(str(new_balance))
    except IOError:
        print("Error: file not found, or there is error in update the amount")


def read_total_expenses():
    total = 0
    expenses_files = []
    for i in os.listdir('.'):
        if i.startswith('expenses') and i.endswith('.txt'):
            expenses_files.append(i)

    for file_name in expenses_files:
        try:
            with open(file_name, 'r') as f:
                for content in f:
                    try:
                        element = content.strip().split(',')
                        if len(element) >= 4:
                            total += float(element[-1])
                    except (ValueError, IndexError):
                        print("can't read the total amount")
        except IOError:
            print(f"can't read the {file_name} file")
    return total


def read_balance():
    balance = read_file()
    expenses = read_total_expenses()
    return balance - expenses


def current_balance():
    balance = read_file()
    expenses = read_total_expenses()
    remain_balance = balance - expenses
    print("Your Current Balance")
    print(f'''
Initial/current balance: ${balance:.2f}
Total expenses to date: ${expenses:.2f}
Available balance: ${remain_balance:.2f}
    ''')

    # ask the uesr if he want to add money
    while True:
        add_money = input("Do you want to add money? [Y/N]").lower()
        if add_money == 'y':
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                print("the amount must be positive")
                continue
            new_amount = balance + amount
            update_balance(new_amount)
            print("The new amount successful added.")
            print(f"The new balance: {new_amount:.2f}")
            break
        elif add_money == 'n':
            break
        else:
            print("Invaild choice only Y or N")


def add_new_amount(new_balance):
    pass


def search_items():
    pass


if __name__ == '__main__':
    while True:
        choice = int(input(
            '''
1) check the remaning balance
2) View Expenseve
3) Add New Expenseve
4) Exit
'''
        ))

        match choice:
            case 1:
                current_balance()
            case 2:
                pass
            case 3:
                pass
            case 4:
                print("Exit from the program")
                break
            case _:
                print("Invaild Choice, try again...")
