# Class6
- [Class6](#class6)
  - [Exercises](#exercises)
  - [Challenge](#challenge)


In this class we are going to work with lists. In python Lists, arrays, and vectors means almost the same thing, and for that reason we are going to treat them as the same thing.

Lists are a collection of information. In some other languages, a list can contain only one type of data. In python, every item can have a different data type, including other lists.

Lists are not a primitive type of data, like strings, and int, and for that reason, we have a different way of working with lists.

In the code below, you will see the main features we use in a list: Declaration, adding item, removing item, getting an item in a specific position, checking if variable is in the list

```python
# Declaration
myList = []

# Adding Item
myList.append('item 1')
myList.append('item 2')

# Removing the first time the item appears
myList.remove('item 1')

# Removing every occurrence of the item in the list
for item in myList:
    if item == 'item 1':
        myList.remove('item 1')

# Getting the item in the specific index
x = myList[0]

# checking if the item is in the list
if 'item 2' in myList:
    print("it's in the list")
```

## Exercises

1. Create a program that reads the number of students in a class, and stores the name of every student
2. Implement a program that calculates the sum of 5 numbers,then prints the numbers and the total sum.

## Challenge

In this challenge, you have to create a program to create a groceries list. The has to be able to achieve the following tasks:

- Add an item, and the quantity
- Change the quantity of an existing item
- Remove an item (remove from the list if the quantity of item is 0 or less)
- print the list in a readable way