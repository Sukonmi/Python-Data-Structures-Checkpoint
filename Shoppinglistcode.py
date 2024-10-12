#1. Create a list named 'shopping_list' to store the items.
# Initialize data structures
shopping_list = []
shopping_tuple = ()
shopping_set = set()
shopping_dict = {}

#2. Use a while loop to create a menu of options for the user to add, remove, or view items from the list.
#  Set maximum number of items
max_items = 5

while True:
    # Display menu
   print("\nMenu:\n1. Add item.\n2. Remove item.\n3. View items.\n4. Exit")
   break

#3. Use the input() function to prompt the user to make a selection from the menu.
    # Get user selection
selection = input("Enter your choice (1-4): ")

    # Handle user selection
if selection == "1":
        # Add item
        if len(shopping_list) < max_items:
            item = input("Enter item to add: ")
            shopping_list.append(item)
            shopping_set.add(item)
            shopping_dict[len(shopping_dict) + 1] = item
            shopping_tuple = tuple(shopping_list)
            print(f"Added '{item}' to the list.")
        else:
            print("List is full.")

elif selection == "2":
        # Remove item
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            shopping_set.discard(item)
            shopping_dict = {k: v for k, v in shopping_dict.items() if v != item}
            shopping_tuple = tuple(shopping_list)
            print(f"Removed '{item}' from the list.")
        else:
            print(f"'{item}' not found in the list.")

elif selection == "3":
        # View items
        print("Shopping List:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")
        print("Shopping Set:", shopping_set)
        print("Shopping Dictionary:", shopping_dict)
        print("Shopping Tuple:", shopping_tuple)

elif selection == "4":
        # Exit
        print("Exiting program.")

else:
        print("Invalid choice.")