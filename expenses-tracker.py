
# Get the balance file path
balance_file_path = 'balance.txt'

# function to read the balance from balance file


def read_file():
    total = 0
    try:
        with open(balance_file_path) as f:
            total = float(f.read())
            print(total)
    except:
        pass
    finally:
        f.close()


def update_balance(new_balance):
    try:
        with open(balance_file_path, 'w') as f:
            f.write(str(new_balance))
    except IOError:
        print("Error: file not found, or there is error in update the amount")


def add_new_amount(new_balance):
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
                read_file()
            case 2:
                pass
            case 3:
                pass
            case 4:
                print("Exit from the program")
                break
            case _:
                print("Invaild Choice, try again...")
