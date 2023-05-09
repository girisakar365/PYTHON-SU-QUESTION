'''
WAP to enter a string and creates a new string that doubles each character of the original strings
'''
string = input("Enter a string: ")

for i in string:
  print(i * 2, end='')