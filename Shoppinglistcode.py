#1. Create a list named 'shopping_list' to store the items.
# Initialize data structures
shopping_list = []
shopping_set = set()
shopping_dict = {}

# 2. Use a while loop to create a menu of options for the user to add, remove, or view items from the list.

while True:
    print("\nMENU: \n1. Add item. \n2. Remove item. \n3. View list. \n4. Exit.")
    break

# 3. Use the input() function to prompt the user to make a selection from the menu.

user_selection = input("Enter your choice (1-4): \n")

# 4. Use an if-elif-else block to determine the user's selection and perform the corresponding action
# a. If the user selects 'add', use the input() function to prompt the user to enter an item to add to the list. Use the range() function to limit the number of items that can be added to the list

max_items = 10

if user_selection == "1":
    for i in range(max_items):
        if len(shopping_list) < max_items:
            item = input("Enter item to add (or 'stop' to finish): ")
            if item.lower() == 'stop':
                break



