"""
WAP that inputs a list, replicates it twice and then prints the sorted list in ascending and descending orders
"""

list = eval(input("Enter a list: "))

list = list * 2

print("replicated list:",list)

list.sort()

print("ascending:",list)

list.sort(reverse=True)

print("decending:",list)
