#!/usr/bin/python

print "------------------------------------------------------------------------------------------------------------------------------------------------------------"

list1 = [1,2,3,4,5,6,7,8,9,9,8,7,6,5,4,3,2,1]
set1 = set(list1)

print list1
print type(list1)

print set1
print type(set1)

set1.add(100)
set1.add(100)
print set1
#set1.remove(100)
print set1
set1.discard(100)
print set1
#set1.remove(100)
set2=set((2,4,6,8,10))

# Print only common elements of sets known as intersection
print (set1 & set2)
print (set1.intersection(set2))

# Print common once & others of the sets known as union
print (set1 | set2)
print (set1.union(set2))

# Print difference between two set
print (set1 - set2)
print (set1.difference(set2))


print (set1 ^ set2)
print set1.symmetric_difference(set2)

print set1.isdisjoint(set2)

print set1.issubset(set2)

print set1.issuperset(set2)

print set1.pop()

print set1.update(set2)
