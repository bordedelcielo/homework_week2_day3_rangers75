# def area_of_a_house(side_a,side_b):
#     side_a = input()
#     the_area = side_a * side_b
#     return f'The area of this house is {the_area} square feet'

# def circumference()

def area_of_a_house():
    while True:
        side_a = int(input('Please provide the length in feet of side a of your house or type "quit" to quit: '))
        if side_a == 'quit':
            break
        # if type(side_a) != int:
        #     side_a = input('Please provide the length in feet of side a of your house as an integer or type "quit" to quit: ')
        side_b = int(input('Please provide the length in feet of side b of your house or type "quit" to quit: '))
        if side_b == 'quit':
            break
        # if type(side_a) != int:
        #     side_a = input('Please provide the length in feet of side a of your house as an integer or type "quit" to quit: ')
        the_area = side_a * side_b
        print(f'The area of this house is {the_area} square feet')
        break

# area_of_a_house()

import math
def circumference():
    while True:
        r_or_d = input("Type 'r' to calculate circumference using a radius, 'd' to calculate circumference using diameter, or 'quit' to quit: ")
        if r_or_d == "r":
            r = int(input("Please enter the radius of the circle you are working with, or type 'quit to quit: "))
            # if r == 'r':
            if r != 'quit':
                ans = (2 * r * math.pi) 
                print(f'The circumference of this circle is {ans}.')
                break
        if r_or_d == "d":
            d = int(input("Please enter the diameter of the circle you are working with, or type 'quit to quit: "))
            # if d == 'd':
            if d != 'quit':
                ans = (d * math.pi) 
                print(f'The circumference of this circle is {ans}.')
                break
        if r_or_d == 'quit':
            break

# circumference()