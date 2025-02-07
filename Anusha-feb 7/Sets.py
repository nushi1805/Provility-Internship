#SETS
# A set is a collection which is unordered, unchangeable*, and unindexed.
#Note: Set items are unchangeable, but you can remove items and add new items.
#Sets are written with curly brackets.
setA = {'charlie','Nick','tao','Elle','Issac'}
print(setA) #Sets are unordered

#Duplicates will be ignored
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

#length of a set
print(len(setA))

#Accessing the set - Cannot be accessed by key or index
# 1. Acessing with loops
for x in setA:
  print(x)

#Specified value can be accessed through "in" keyword
print("tao" in setA)
#to check if the item is not in the set
print("Darcy"  not in setA)

#Add set items
#add() is used to add items into the set
setA.add('Darcy')
print(setA)

#2.Adding set to a set - bu using update() keyword
setB= {'Tara','Ben','Imogen','Tori'}
setA.update(setB)
print(setA) #Here the object which is updated need not be a set instead can be any iterable objects

#Loops in set - We cannot use while loop in sets since they dont have index but for loops can be used since they iterate over each element
for x in setA:
  print(x)

# JOINING SETS

# union() - Joins all items from both sets and returns a new set
setA = {'charlie', 'Nick', 'tao', 'Elle', 'Issac'}
setB = {'Darcy', 'Tara', 'Ben', 'Tori'}
setC = {'Imogen', 'Mr. Ajayi', 'Coach Singh'}

# Joining using union()
new_set = setA.union(setB, setC)
print(new_set)

# Joining using | operator
new_set = setA | setB | setC
print(new_set)

# Joining a set with a tuple using union()
extra_characters = ("Alastair", "Harry")
merged_set = setA.union(extra_characters)
print(merged_set)

# update() - Inserts all items from one set into another
setA.update(setB)
print(setA)

# INTERSECTION

# intersection() - Returns a new set with items present in both sets
setA = {'charlie', 'Nick', 'tao', 'Elle', 'Issac'}
setB = {'Nick', 'Tao', 'Ben', 'Tori'}
common_items = setA.intersection(setB)
print(common_items)

# Using & operator
common_items = setA & setB
print(common_items)

# intersection_update() - Modifies the original set to keep only common items
setA.intersection_update(setB)
print(setA)

# DIFFERENCE

# difference() - Returns a new set with items from the first set not in the second
setA = {'charlie', 'Nick', 'tao', 'Elle', 'Issac'}
setB = {'Nick', 'Tao', 'Ben', 'Tori'}
unique_items = setA.difference(setB)
print(unique_items)

# Using - operator
unique_items = setA - setB
print(unique_items)

# difference_update() - Modifies the original set to remove items found in the other
setA.difference_update(setB)
print(setA)

# SYMMETRIC DIFFERENCE

# symmetric_difference() - Returns a new set with items not present in both sets
setA = {'charlie', 'Nick', 'tao', 'Elle', 'Issac'}
setB = {'Nick', 'Tao', 'Ben', 'Tori'}
symmetric_diff = setA.symmetric_difference(setB)
print(symmetric_diff)

# Using ^ operator
symmetric_diff = setA ^ setB
print(symmetric_diff)

# symmetric_difference_update() - Modifies the original set to keep only unique items
setA.symmetric_difference_update(setB)
print(setA)

