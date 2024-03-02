#Ask the user for a list of five integers. Store them in an array. Sort the list and display it in reverse order.

from array import *

nums = array('i',[])

for i in range(0,5):
    num = int(input("Enter a number: "))
    nums.append(num)

nums = sorted(nums)

nums.reverse()

print(nums)