# remove and discard
set1 = {1, 2, 3, 4}

set1.remove(1)
print("remove", set1)

set1.discard(1)
print("discard", set1)

# difference and difference_update
set2 = {5, 6, 7, 8}

set2.difference(set1, set2)
print("difference", set2)

set2.difference_update(set1, set2)
print("difference_update", set2)

#insersection and intersection_update
set3 = {9, 10, 11, 12}

set3.intersection(set1)
print("insertion", set3)

set3.intersection_update(set1)
print("insertion_update", set3)

# symmetric_difference and symmertic_update_difference
set4 = {13, 14, 15, 16}

set4.symmetric_difference(set3)
print("symmetric_difference", set4)

set4.symmetric_difference_update(set3)
print("symmetric_difference_update", set4)
