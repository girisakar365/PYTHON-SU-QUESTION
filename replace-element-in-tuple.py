"""
3.	A tuple tl stores (11,21,31,42,51), where its second last element is mistyped. Write a program to correct its second last element as 41
"""

t1 = (11, 21, 31, 42, 51)
t1 = list(t1)
t1[-2] = 41
t1 = tuple(t1)

print(t1)
