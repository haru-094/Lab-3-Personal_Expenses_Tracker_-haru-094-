# function to show the menu

def show_menu():
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
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            print("Exist from the program")
            exit
        case _:
            print("Invaild Choice, try again...")

# show_menu()

# read data from file.txt

def read_file():
    pass


