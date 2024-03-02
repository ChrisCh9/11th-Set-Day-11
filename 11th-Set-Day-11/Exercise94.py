#Display an array of five numbers. Ask the user to select one of the numbers. Once they have selected a number, display the position of that item in the array. If they enter something that is not in the array, ask them to try again until they select a relevant item.

from array import *

nums = array('i',[4,6,8,2,5])

for i in nums:
    print(i)

num = int(input("Select one of the numbers: "))

try_again = True

while try_again == True:
    if num in nums:
        print("This is in position", nums.index(num))
        try_again = False
    else:
        print("That's not a value in the array")
        num = int(input("Select one of the numbers: "))