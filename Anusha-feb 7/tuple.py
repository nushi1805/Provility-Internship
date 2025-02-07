#TUPLES
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
tuplee = ('Damon','Stefan','Kathrine','Lexi','Elena')
print(tuplee)
#length of a tuple
print(len(tuplee))

#To create tuple with single value comma (,) should be included after the item , if not it wont be considered as tuple
onetuple=('hello')
print (type(onetuple)) #considered as str

onetuple=('hello',)
print (type(onetuple))

#Tuple constructor
mytuple = tuple(("apple", "banana", "cherry"))
print(mytuple)

#Acessing tuples
#index
print(tuplee[0])
#reverse index
print(tuplee[-1])
#range of index
print(tuplee[1:4])
print(tuplee)

#updating the tuple
#tuples are unchangable meaning elements cannot be added or deleted after creating the tuple
#Two ways to manipulate tuples indirectly
#1.Converting to list
y = list(tuplee)
tupleee = ('bonnie','klaus','caroline')
y.append('bonnie')
tuplee= tuple(y)
print(y)
#2. Adding tuple to tuple
tupleeee= tuplee + tupleee
print(tupleeee)

#tuple packing - assigning values is called tuple packing
#tuple unpacking
(green , *hello ,blue) = tuplee
print (green)
print (hello)
print (blue)

#loops in tuple
tuplee = ('Damon','Stefan','Kathrine','Lexi','Elena')
for x in tuplee:
  print(x)

#with index number
for i in range(len(tuplee)):
  print(tuplee[i])

#while loop
i = 0
while i < len(tuplee):
  print(tuplee[i])
  i = i + 1

#joining two list
#1.Addition operation
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
#2.Multiplying tuples
new_tuple= tuplee*2
print(new_tuple)

#count()
x =new_tuple.count('Damon')
print(x)
