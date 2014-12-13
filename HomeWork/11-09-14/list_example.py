#!/usr/bin/python

list1 = [0,1,2,3,4,5,6,7,8,9]
list2 = [9,8,7,6,5,4,3,2,1,0]

print list1[2:]

print list2[:5]

list3 = list1 + list2

print list3

# List are mutable
list3[0] = 1000

print list3

# Removed elements form 2th position to 7th position
list3[2:7] = []

print list3

# Size/Length of list
print len(list3)

# Create a list which contains list

list1.sort()
list2.sort()
list3.sort()

list4 = [list1, list2, list3]

list1.reverse()
list2.reverse()
print list4



