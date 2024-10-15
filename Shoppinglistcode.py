#1. Create a list named 'shopping_list' to store the items.
# Initialize data structures
shopping_list = []
unique_items = set()
item_info = {}
our_store_items = {"Mango":5, 
                   "Apple":10, 
                   "Pear":4, 
                   "Pineapple":30, 
                   "Orange":5,
                   "Banana":20,
                   "Watermelon":15,
                   "Strawberry":65,
                   "Blueberry":35,
                   "Kiwi":55,
                   "Tangerine":7}

# 2. Use a while loop to create a menu of options for the user to add, remove, or view items from the list.

while True:
    print(""" Shopping list Menu
            1. Add item.
            2. Remove item.
            3. View item.
            4. Exit""")

# 3. Use the input() function to prompt the user to make a selection from the menu.

    user_selection = int(input("Enter your choice (1-4): \n"))

# 4. Use an if-elif-else block to determine the user's selection and perform the corresponding action
# a. If the user selects 'add', use the input() function to prompt the user to enter an item to add to the list. Use the range() function to limit the number of items that can be added to the list

    if user_selection == 1:
        print("Proceed to add items to your cart")
        print("This are our available items:")
        for item in our_store_items.keys():
            print(item)
        for i in range(5):
            item = input("Select an item or input [Checkout] to leave this menu: ").capitalize()
            if item == "Checkout":
                break
            if item in our_store_items:
                if item in unique_items:
                    print("Item already exist. \nSelect another item: ")
                else:
                    item_quantity = int(input(f"How many {item}s do you want? "))
                    shopping_list.append(item)
                    unique_items.add(item)
                    item_info[item] = item_quantity
                    item_info[f"{item}_price"] = our_store_items[item] * item_quantity
                    print(f"Your {item}(s) have been added to your cart")
            else:
                print("Sorry we do not have this currently.")

# If the user selects 'remove', use the input() function to prompt the user to enter an item to remove from the list.
    elif user_selection == 2:
        print("Proceed to removing items from your cart")
        for removables in shopping_list:
            print(removables)
        selected_item = input("What item(s) do you want to remove: \n")
        if selected_item in shopping_list:
            shopping_list.remove(selected_item)
        if selected_item in unique_items:
            unique_items.pop(selected_item)
        else:
            print("Selected items are not present in your cart")