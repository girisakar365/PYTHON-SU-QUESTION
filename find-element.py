"""
WAP to search for an element in a given list of numbers
"""

list = input("Enter a list: ").split(",")

element = input("enter the element to find: ")
print("Index of",element,"=",list.index(element))