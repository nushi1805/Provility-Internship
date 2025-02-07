"""fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
Get the first three elements.
2. Get the last three elements.
3. Reverse the entire list using slicing.
---------------
Create a list containing numbers from 1 to 20.
Use list comprehension to create a new list containing only the even numbers.
Print the result.
---------------
a = 5
b = 10
swap values without temp variables using list unpacking"""

fruits =["apple","banana","cherry","date","elderberry","fig","grape"]
print("First three elements =",fruits[:3])
print("Last three elements =",fruits[4:])
print("Reversed List=", fruits[::-1])

List=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
newList= List[1::2]
print("List with even nos =" ,newList)


a , b = 5 , 10
a , b = b , a
print("A , B =",a,b)
