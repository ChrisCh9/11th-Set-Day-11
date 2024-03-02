#Create two arrays (one containing three numbers that the user enters and one containing a set of five random numbers). Join these two arrays together into one large array. Sort this large array and display it so that each number appears on a separate line.

from array import *
import random

num1 = array('i',[])

num2 = array('i',[])

for i in range(0,3):
    num = int(input("Enter a number: "))
    num1.append(num)

for i in range(0,5):
    num = random.randint(1,100)
    num2.append(num)

num1.extend(num2)

num1 = sorted(num1)

for i in num1:
    print(i)