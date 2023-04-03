shopping_list = []

def add_item(item):
    shopping_list.append(item)
    print(item, "added to shopping list.")

def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(item, "removed from shopping list.")
    else:
        print(item, "not found in shopping list.")

def view_list():
    print("Shopping List:")
    for item in shopping_list:
        print("-", item)

while True:
    print("\n1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Quit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        item = input("Enter item to add: ")
        add_item(item)
    elif choice == "2":
        item = input("Enter item to remove: ")
        remove_item(item)
    elif choice == "3":
        view_list()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Try again.")
