"""
WAP to count the frequency of a given element in a list of numbers without using count() method.
"""
list = input("Enter a list: ").split(",")

element = input("Enter an element inside list: ")

count = 0

for i in list:
  if i == element:
    count += 1

print("count of", element, "=", count)
