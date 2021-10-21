# Find Even numbers
# Create a function that, given a list as a parameter, finds the even numbers inside the list. The function should then return a list.
# Example:
# Input: [2, 7, 10, 11, 12]
# Output: [2, 10, 12]

def getEvens(someList):
    return [x for x in someList if x % 2 ==0]

# def getEvens2(someList):
#     result


l1 = [2, 7, 10, 11, 12]
print(getEvens(l1))