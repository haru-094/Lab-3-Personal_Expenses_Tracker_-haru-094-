import os
import sys
from datetime import datetime


# Get the balance file path
balance_file_path = 'balance.txt'

# Function that read the balance file


def read_balance_file():
    """
    Function that read the data exist in balance.txt
    if not exist it will created and initailze the value to 0 as start point
    """
    if not os.path.exists(balance_file_path):
        try:
            with open(balance_file_path, 'w') as f:
                f.write('0.0')
        except IOError:
            print("can't create the file")
            sys.exit(1)
        return 0.0

    try:
        with open(balance_file_path, 'r') as f:
            total = f.read().strip()
            if not total:
                return 0.0
            return float(total)
    except IOError:
        print("Error, can't read the balance file")
        sys.exit(1)


def update_balance(new_balance):
    """
    Function that update the balance it take new_balance as parameter
    and then update the value in balance file
    """
    try:
        with open(balance_file_path, 'w') as f:
            f.write(str(new_balance))
    except IOError:
        print("Error: file not found, or there is error in update the amount")


def read_total_expenses():
    """
    Function that read all the expenses that have you done so far
    every expenses file that created
    """
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
                        # print("can't read the total amount")
                        continue
        except IOError:
            print(f"can't read the {file_name} file")
    return total


def read_balance_amount():
    balance = read_balance_file()
    expenses = read_total_expenses()
    return balance - expenses


def current_balance():
    """
    Fucntion that get the current balance then ask the user and prompt
    if he want to add money
    """
    balance = read_balance_file()
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
        add_money = input("Do you want to add money? [Y/N]\n").lower()
        if add_money == 'y':
            try:
                amount = float(input("Enter the amount: \n").strip())
            except ValueError:
                print("amount is not number")
                continue
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


def add_new_expense():
    """
    Function that add new expenses with the data it ask the user for 3
    the name of item, the price, the date then it will add for in new file
    """
    balance = read_balance_amount()
    print("Add New Expenses")
    print(f"Your current balance {balance}")

    while True:
        date = input("Enter the data in format of YYYY-MM-DD: \n")
        try:
            datetime.strptime(date, '%Y-%m-%d')
            break
        except ValueError:
            print("Invaild date must be in this format YYYY-MM-DD")

    name = input("Enter the name of item: \n")

    if not name:
        print("Error, the item must not be empty")
        return

    while True:
        try:
            price = float(input("Enter the item price: \n"))
            if price <= 0:
                print("The amount must be positive")
                continue
            else:
                break
        except ValueError:
            print("Error, the amount must be integer")

    print("confirmation [y/n]\n")
    print(f"""
    item name: {name}
    amount: {price:.2f}
    date: {date}
    """)
    confirm = input("Are the data correct? [Y/N] \n").strip().lower()

    if confirm == 'y':
        if price > balance:
            print("Error, Insufficient balance! Cannot save expense.")
            return
        file_name = f"expenses-{date}.txt"
        item_id = 1
        if os.path.exists(file_name):
            try:
                with open(file_name, 'r') as f:
                    item_id = len(f.readlines()) + 1
            except IOError:
                print("Error, can't create unique ID")
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        item_expense = f"{item_id},{current_date},{name},{price:.2f}\n"

        # create or append the item into file
        try:
            with open(file_name, 'a') as f:
                f.write(item_expense)
        except IOError:
            print("Error, can't save the file")
            return
        # init_balance = read_balance_file()
        # new_balance = init_balance - price
        # update_balance(new_balance)

        remain_balance = read_balance_amount()
        print("Expense added")
        print(f"The remaining balance: {remain_balance:.2f}")
    elif confirm == 'n':
        print("Not adding")
    else:
        print("Invaild choice, enter Y or N")


def view_search_expenses():
    """
    Function that will search for item or price then return the result if it exist
    it will show menu then prompt the user
    """
    print("""
1. Search by item name
2. Search by amount
3. Back to main menu
        """)
    while True:
        try:
            choice = int(input("choice from [1-3]\n"))
        except ValueError:
            print("Error, need to be from 1 to 3")
            continue
        # search for item name
        if choice == 1:
            item_name = input("Enter the name of item: \n").strip().lower()
            if item_name:
                print(f"Match found of {item_name}")
                match_found = 0
                expenses_files = []
                for i in os.listdir('.'):
                    if i.startswith('expenses') and i.endswith('.txt'):
                        expenses_files.append(i)

                for file_name in expenses_files:
                    try:
                        with open(file_name, 'r') as f:
                            for content in f:
                                element = content.strip().split(',')
                                if len(element) >= 4:
                                    item = element[2].lower()
                                    if item_name in item:
                                        print(
                                            f"{file_name} : {content.strip()}")
                                        match_found += 1
                    except IOError:
                        print(f"can't read the {file_name} file")
                if match_found == 0:
                    print("item not found")
            else:
                print("item must not be empty")
        # search for the item price
        elif choice == 2:
            try:
                price_item = float(
                    input("Enter the amount of item: \n").strip())
            except ValueError:
                print("the amount need to be number")
                continue
            print(f"Match found of {price_item}")
            match_found = 0
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
                                    price = float(element[-1])
                                    if price == price_item:
                                        print(
                                            f"{file_name} : {content.strip()}")
                                        match_found += 1
                            except ValueError:
                                continue
                except IOError:
                    print(f"can't read the {file_name} file")
            if match_found == 0:
                print("item not found")
        # exit from the menu and return the main menu
        elif choice == 3:
            break
        else:
            print("Error, only choice from 1 to 3")


# main function
if __name__ == '__main__':
    while True:
        try:
            choice = int(input(
                '''
1) check the remaning balance
2) View Expenseve
3) Add New Expenseve
4) Exit
'''
            ).strip())
        except ValueError:
            print("Error must be from 1 to 4 only")
            continue
        match choice:
            case 1:
                current_balance()
            case 2:
                view_search_expenses()
            case 3:
                add_new_expense()
            case 4:
                print("Exit from the program")
                break
            case _:
                print("Invaild Choice, try again...")
