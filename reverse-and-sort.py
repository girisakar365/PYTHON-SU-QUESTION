"""
WAP that inputs a list, replicates it twice and then prints the sorted list in ascending and descending orders
"""

input_list = input("Enter a list: ").split(",")

list = []

for i in input_list:
  list.append(int(i))

print([list] * 2)

list.sort()

print("ascending:",list)

list.sort(reverse=True)

print("decending:",list)