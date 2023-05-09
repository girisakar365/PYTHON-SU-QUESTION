"""
4.	WAP to read a sentence and then create a dictionary contains the frequency of letters and digits in the sentence.
"""
sentence = input("Enter a sentence: ")
dict = {}

for i in sentence:
  dict[i] = sentence.count(i)

print(dict)