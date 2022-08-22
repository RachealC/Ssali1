#1. Print First 10 natural numbers using while loop.
from re import I


i = 1
while(i<=10):
    print(i)
    i += 1
#2. Calculate the sum of all numbers from 1 to a given number.
sum = 0
counter = 1
n = int(input("Enter the value of n: "))
    # calculate sum of first n natural numbers
while counter <= n:
        sum = sum + counter
        counter = counter + 1
        print("The sum is: ", sum)

#3. Write a program to print multiplication table of a given number. eg if number is 2, then output should be 2, 4, 6, 8 ...

num = int(input("Enter the number: "))
print("Multiplication Table of", num)
for i in range(1, 11):
   print(num,"X",i,"=",num * i)     

#4. Write a program to display only those numbers from a list that satisfy the following conditions
#The number must be divisible by 5
#If the number is greater than 150, then skip it and move to the next number
#If the number is greater than 500, then stop the loop
#given `numbers = [12, 75, 150, 180, 145, 525, 50]`

numbers = [12, 75, 150, 180, 145, 525, 50]
# iterate each i of a list
for i in numbers:
    if i > 500:
        break
    elif i > 150:
        continue
    # check if number is divisible by 5
    elif i % 5 == 0:
        print(i)
#5.  Write a program to count the total number of digits in a number using a while loop. given number `4673453` Display numbers from -10 to -1 using while loop
# len() return the size of a list or any iterable sequence
num = '4673453'
print(len(str(num)))
