# function to show the menu

def show_menu():
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
                read_file('balance.txt')
            case 2:
                pass
            case 3:
                pass
            case 4:
                print("Exit from the program")
                break
            case _:
                print("Invaild Choice, try again...")


# read data from file.txt


def read_file(filename):
    try:
        file = open(filename, 'r')
        file_content = file.read()
        print(file_content)
        print("Do you want to add new amount? [Yes, No]\n")

    except:
        pass
    finally:
        file.close()


def update_balance(new_balance):
    try:
        with open('balance.txt', 'w') as f:
            f.write(str(new_balance))
    except IOError:
        print("Error: file not found, or there is error in update the amount")


def add_new_amount(new_balance):
    pass
