# my first pass
import os
def shopping_cart():
    my_cart = []

    while True:
        # print message: "Your shopping cart is currently empty."
        # set variable name and create input statement.
        if my_cart == []:
            shopping_item = input("Your shopping cart is currently empty. Please enter an item you wish to add, or type 'quit' to quit:")
        if my_cart == [] and shopping_item != 'quit' and shopping_item != '':
            my_cart.append(shopping_item)
        if my_cart !=[]:
            shopping_item = input(f"Your shopping cart currently contains the following items: {my_cart}. Please enter an item you wish to add, type 'delete' to select an item to remove from your shopping cart, or type 'quit' to quit:")
        if shopping_item != 'quit' and shopping_item != 'delete' and shopping_item != '':
            my_cart.append(shopping_item)
        if shopping_item == '':
            continue
        if shopping_item == 'delete':
            item_to_remove = input("Which item would you like to remove?")
            my_cart.remove(item_to_remove)
        if shopping_item == 'quit':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'Your final list contains the following items: {my_cart}')
            break

shopping_cart()

# 1) Build a Shopping Cart
# You can use either lists or dictionaries. The program should have the following capabilities:

# 1) Takes in input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, print out all items in the user's list

# import os
# def shopping_cart():
#     my_cart = []

#     while True:
#         print message: "Your shopping cart is currently empty."
#         set variable name and create input statement.
#         if my_cart == []:
#         shopping_item = input("Your shopping cart is currently empty. Please enter an item you wish to add.")
#         shopping_item = input("Enter the item you wish to add to your shopping cart or type 'quit': ")
#         if shopping_item == 'quit':
#             os.system('cls' if os.name == 'nt' else 'clear')
#             print(f'Your final list contains the following items: {my_cart}')
#             break
#         my_cart.append(shopping_item)

# shopping_cart()

# Giving more options. Anticipate anything the user may input.
# Think of each action as a "method" in the "class" of the shopping cart.
# You can have tiered options from the beginning
# What would you like to do? --> Add, Delete, Show Items, Quit
# Think about how to give more choices, more options. Based off of first input, provide another conditional.
# e.g., if action = add: another thing says "What would you like to add?" set to "response" variable.
# "Nested conditionals"