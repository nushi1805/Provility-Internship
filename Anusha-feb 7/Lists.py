#Lists - It is used to store multiple items in a single variable
#Created using square brackets [] - Orderd , changable and allow duplicateb values
#One of the 4 data types in python - List , Tuple, Dictionary ,Sets

List = ['Conrad','Belle','Jermiah',]
print(List)

#Length of a list
print(len(List))

#Accessing the List- Done by mentioning index . index starts from 0
List = ['Conrad','Belle','Jermiah','Kitty' ,'Minho']
print(List[0])
#Negative indexing is used to access the list from the end . Index starts from -1
print(List[-1])
#Range of indexes
print(List[3:5])

#Changing items value in the list
List = ['Conrad','Belle','Jermiah','Kitty' ,'Minho']
List[0]='Yuri'
print(List)

#To update range of items in a list, assign new values to a range of indices
List[1:3] =['Q','Juliana']
print(List)
#Inserting more items shifts the remaining items to the right
List[3:5] = ['Dae','Eunice','Stella']
print(List)
#Inserting less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
List[3:6]=['Minho','Kitty']
print(List)

#To insert elements without replacing .insert() is to be used along with the index number of where it needs to be inserted
List.insert(3,'Dae')
List.insert(4,'Eunice')
print(List)

#Append() is used to append elements at the end of the list
List.append('Jae')
print (List)
#insert is used one inserting need to be done at a specific index and append when needs to be done at end.

#Extend() is used when one list need to be appended at the end of another list.
#The other one can be of any type-Dictionary,Sets ,Lists , Tuples

XOK = ['Yuri', 'Q', 'Juliana', 'Dae', 'Eunice', 'Minho', 'Kitty']
TSIP = ['Conrad','Belle','Jermiah']
XOK.extend(TSIP)
print(XOK)
tsip = ('Tyler' , 'Stevan')
XOK.extend(tsip)
print(XOK)

#remove() method removes the specified item form the list-it removes only one item and cannot be removed by index
XOK.remove('Jermiah')
print(XOK)

#del statement deletes the elements through index
del XOK[7:]
print(XOK)

XOK.pop(2)
print(XOK)

XOK.clear()
print(XOK)

del XOK

#Looping through list
#printing all the items in the list
for i in List:
    print(i)
print("...................................................................................................")
for i in List[3:7]:
    print(i)
print("...................................................................................................")
i = 0
while i < len(List):
  print(List[i])
  i = i + 1

#List Comprehension - Shorter Syntax
#SYNTAX FOR LIST COMPREHENSION ---  newlist = [expression 'for' item 'in' iterable 'if' condition == 'True'
#expression: What you want to do with each item.
#item: The current element from the iterable.
#iterable: Any iterable (like a list, range, string, etc.).
#+if condition (optional): Filters which items to include.
[print (x) for x in List]
print("...................................................................................................")

#WithoutList comprehension
print(List)
New_List =[]
for i in List:
    if 'a' in i:
        New_List.append(i)
print(New_List)

#With List comprehension
newlist = [x for x in List if 'a' in x]
print(newlist)

#Sorting
#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
List.sort()
print( "Sorted List:",List)

#To sort descending, use the keyword argument reverse = True
List.sort(reverse=True)
print("Reversed List=",List)

#customixing sorting with function by using the keyword argument "key = function"
def myfn(n):
    return abs(n-50)
numlist=[33,78,65,54,72,22,50,51]
print("Before sorting :",numlist)
numlist.sort(key = myfn)
print("After Sorting : " ,numlist)

#The reverse() method reverses the current sorting order of the elements.
numlist.reverse()
print(numlist)
List.reverse()
print(List)

#Copying the list - Can be done with copy() , list() and slice operator
#Copy()
Copylist = List.copy()
print(Copylist)
#list()
Copylist1 = list(List)
print(Copylist1)
#Using slice operator
Copylist2 = List[::]
print(Copylist2)

#Joining two list-
#1. using '+' operator
alphabets1 = ['a','b','c','d','e','f','g','h']
alphabets2 = ['i','j','k','l','m','n','o','p']
alphabets = list(alphabets1 + alphabets2)
print(alphabets)
#2. append() -append method returns none .It just manipulates the given list . Prints the entire list as one element
alphabets1.append(alphabets2)
print(alphabets1)
#3. extend() - returns none, adds elements individually to the list
alphabets1.extend(alphabets2)
print (alphabets1)




