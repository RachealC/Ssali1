#1. Write a Python program to sum all the items in a list.
# The list should be generated using list comprehension
#- The size of the list should be from a user input

# generating list
num = [ x for x in range(20) if x % 2 == 0]
print(num)

#sum
num = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
sum_of_num = sum(num)
print(sum_of_num)

#2. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Sample List : `['abc', 'xyz', 'aba', '1221']`

def match_words(words):  
  ctr = 0  
  
  for word in words:  
    if len(word) > 1 and word[0] == word[-1]:  
      ctr += 1  
  return ctr  
  
print(match_words(['abc', 'xyz', 'aba', '1221']))  

#3. Write a Python program to remove duplicates from a list, given list

fruits = ["Apple", "Banana", "Melon", "Banana", "Cherry", "Banana"]
del fruits[2:4]

print(fruits) # ['Apple', 'Melon', 'Cherry']

#4. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Sample List : `['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']`

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)
#5. Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included)

def printValues():
	l = list()
	for i in range(1,31):
		l.append(i**2)
	print(l[5:])
printValues()