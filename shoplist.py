import os
import platform
from time import sleep

shopping_list = []

def clear():
    """Clears the terminal"""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def stay_or_back():
    """Asks the user to stay or go back to the main menu"""
    while True:
        try:
            clear()
            choice = int(input("Would you like to stay or go back? [1] Stay  [2] Back: "))
            if choice == 1:
                clear()
                break
            elif choice == 2:
                print("Returning to main menu...")
                sleep(1)
                return False
            else:
                print("Only 1 or 2 are allowed!")
                sleep(1)
        except ValueError:
            print("Error: only numbers are valid!")
            sleep(1)

def menu():
    """Shows the main menu"""
    print("=== SHOPPING LIST ===")
    print("1 - Add item")
    print("2 - Show list")
    print("3 - Remove item")
    print("4 - Exit")
    selection = int(input("Choice: "))
    return selection

def add_item():
    """Adds an item to the shopping list"""
    while True:
        try:
            clear()
            item = input("Type your item: ").strip().upper()

            if item == "":
                print("Item cannot be empty!")
                sleep(1)
                continue

            if item in shopping_list:
                print(f"{item} is already in the list!")
                sleep(1)
            else:
                shopping_list.append(item)
                print(f"{item} added successfully!")
                sleep(1)

            result = stay_or_back()
            if result == False:
                break
        except TypeError:
            print("Error, try again!")
            sleep(1)

def show_list():
    """Shows all items in the shopping list"""
    clear()
    print("=== YOUR LIST ===")
    for i, item in enumerate(shopping_list, start=1):
        print(f"{i}. {item}")
    print("=================")
    while True:
        exit_input = input("Press Enter to go back: ")
        if exit_input == "":
            clear()
            break
        else:
            print("Just press Enter!")

def remove_item():
    """Removes an item from the shopping list"""
    while True:
        clear()
        if not shopping_list:
            print("The list is empty, nothing to remove!")
            sleep(2)
            break

        print("=== REMOVE ITEM ===")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")
        print("===================")

        try:
            choice = int(input("Type the number of the item to remove (0 to cancel): "))

            if choice == 0:
                print("Cancelled!")
                sleep(1)
                break
            elif 1 <= choice <= len(shopping_list):
                removed = shopping_list.pop(choice - 1)
                print(f"{removed} removed successfully!")
                sleep(1)

                result = stay_or_back()
                if result == False:
                    break
            else:
                print(f"Type a number between 1 and {len(shopping_list)}!")
                sleep(1)
        except ValueError:
            print("Error: only numbers are valid!")
            sleep(1)

def validation_treatment():
    """Main loop that handles user choices"""
    while True:
        try:
            clear()
            selection = menu()
            match selection:
                case 1:
                    add_item()
                case 2:
                    if not shopping_list:
                        print("The list is empty, add some items first!")
                        sleep(2)
                        clear()
                    else:
                        show_list()
                case 3:
                    remove_item()
                case 4:
                    clear()
                    print("Okay, bye!")
                    sleep(1)
                    break
                case _:
                    print("Invalid option, try again!")
                    sleep(1)
                    clear()
        except ValueError:
            print("Error: type a number from 1 to 4!")
            sleep(1)
            clear()

def main():
    validation_treatment()

if __name__ == "__main__":
    main()