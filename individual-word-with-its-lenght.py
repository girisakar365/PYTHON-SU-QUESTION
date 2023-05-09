'''
WAP to enter a string and print individual word of string along with its length
'''
sentence = input("Enter any sentence: ")

for i in sentence.split(" "):
  print(i, "Lenght = ", len(i))
