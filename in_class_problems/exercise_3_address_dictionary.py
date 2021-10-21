# Following along with John Loveland's in class solution
# Step 1
def store_info():
    info = {}

    #step 3. while True runs until it hits a break condition. cmds are built on while True loops.
    # Build user interface early to test code easily with user interface.
    import os
    while True:
        #set variable name and add input statement.
        name = input("Enter a name to be stored or type 'quit': ")
        if name == 'quit':
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        address = input("Enter an address to be stored or type 'quit': ")
        if address == 'quit':
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        info[name] = address
    
    # iterate over dictionary
    for key, value in info.items():
        print(f'The address for {key} is {value}')

store_info()

# step 1: write a function that takes in information and stores it in a dictionary
# step 2: define an empty dictionary to work with
# step 3: create our loop, which asks the user for information until they quit
# step 4: ask for the information, and store it into variables
# step 5: check if the user types quit
# step 5a: print out all information
# step 5b: break out of the loop
# step 6: if they didn't quit, add the information to the dictionary
# step 7: invoke the function by calling it

# def printInput(answer):
#     print(answer)

# response = input('Are you ready to quit??')

# while True:
#     ask = input('What do you want to do?')
    
#     printInput(ask)
    
#     response = input('Ready Yet?')
#     if response.lower() == 'quit':
#         break

# import os
# # instead of import clear_output
# def address_book():
#     entries = {}
#     while True:
#         name = input("Enter a name to be stored or say 'quit': ")
#         if name.lower() == 'quit':
#             for key,value in entries.items():
#                 print(f"The Address for {key} is {value}")
#             break
#         address = input("Enter an address to be stored or say 'quit': ")
#         os.system('cls' if os.name == 'nt' else 'clear')
#         # instead of clear_output in Jupyter Notebook

#         # Why can't the below be an or statement?
#         # if name.lower() == 'quit' and address.lower() == 'quit':
#         #     for key,value in entries.items():
#         #         print(f"The Address for {key} is {value}")
#         #     break
#         entries[name] = address
# address_book()

# import os
# os.system('cls' if os.name == 'nt' else 'clear')