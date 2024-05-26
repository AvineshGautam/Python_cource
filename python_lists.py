"""
Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary.
List items are ordered, changeable, and allow duplicate values.

"""
# my_list1 = ["apple",1,True,False,]
# print(my_list1)                      #List items can be of any data type
# print(len(my_list1))                 #len() is for length of the lists
# print(type(my_list1))                #type() lists are defined as objects with the data type 'list'
# print(my_list1[1])                  # for indexing 


# list constructor --> It is also possible to use the list() constructor when creating a new list.
# my_list2 = (("apple","mango","apple",True,1,False))     # Note:- note the double round-brackets and lists can hold duplicates value also
# print(my_list2)

# Access List Items --> List items are indexed and you can access them by referring to the index number:
# my_list = ["avi","udit","deepak","sonu","ankur",True,5,"kaku"]
# print(my_list[2])                           # indexing starts from 0
# print(my_list[2:5])                         # called Range of index --> Note: The search will start at index 2 (included) and end at index 5 (not included).
# print(my_list[-1:-3])                       # Gives empty list i.e [] coz start index should less then end index in this case -1 is greater then -3

# Slicing Syntax: list[start:end:step]
# print(my_list[1:7:3])                       # default step is 1
# print(my_list[:3])
# print(my_list[4:])
# print(my_list[::-1])                        # Output: ['kaku', 5, True, 'ankur', 'sonu', 'deepak', 'udit', 'avi']
# print(my_list[-1:-5:-1])                    # Output: ['kaku', 5, True, 'ankur']
# print(my_list[::2])

# Check if Item Exists
# if "udit" and True in my_list:
#     print("Yes")
# else:
#     print("No")


# Change List Items
# my_list = ["avi","udit","deepak","sonu","ankur",True,5,"kaku"]
# my_list[2]=False                                                    # By using or refer to the index number
# my_list[0:2]=["praveen",5]                                            # Can change using Range Items
# print(my_list)

# Insert Items --> The insert() method inserts an item at the specified index
# my_list = ["avi","udit","deepak","sonu","ankur",True,5,"kaku"]
# my_list.insert(2,"rahul")                                              # (2, "rahul")--> 2 is index number and rahul will place on index 2
# print(my_list)

# Add List Items --> To add an item to the end of the list, use the append() method.
# my_list = ["avi","udit","deepak","sonu","ankur",True,5,"kaku"]
# my_list.append("praveen")                                               # append function will take only one argument
# print(my_list)

# Extend List --> To append elements from another list to the current list, use the extend() method.
# my_list1 = ["avi","udit","deepak","sonu","ankur",True,5,"kaku"]
# my_list2 = [1,5,True,"mango",False]
# my_list1.extend(my_list2)
# print(my_list1)

# Note --> The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
# my_list1 = ["avi","udit","deepak","sonu","ankur",True,5,"kaku"] # List
# my_list2 = ("praveen","rahul",5)                                # Tuple
# my_list1.extend(my_list2)
# print(my_list1)

# Remove List Items --> The remove() method removes the specified item.
# my_list = ["avi","udit","deepak","sonu","avi","ankur",True,5,"kaku"]
# my_list.remove("kaku")
# my_list.remove("avi")                               # If there are more than one item with the specified value, the remove() method removes the first occurance
# print(my_list)

# The pop() method removes the specified index.
# my_list = ["avi","udit","deepak","sonu","avi","ankur",True,5,"kaku"]
# my_list.pop(2)
# print(my_list)

# If you do not specify the index, the pop() method removes the last item.
# my_list = ["avi","udit","deepak","sonu","avi","ankur",True,5,"kaku"]
# my_list.pop()
# print(my_list)

# The del keyword also removes the specified index:
# my_list = ["avi","udit","deepak","sonu","avi","ankur",True,5,"kaku"]
# del my_list[2]
# print(my_list)

# The del keyword can also delete the list completely.
# my_list = ["avi","udit","deepak","sonu","avi","ankur",True,5,"kaku"]
# del my_list
# print(my_list)

# The clear() method empties the list.
# The list still remains, but it has no content.
# my_list = ["avi","udit","deepak","sonu","avi","ankur",True,5,"kaku"]
# my_list.clear()
# print(my_list)

# Loop Through a List
# my_list = ["avi","udit","deepak","sonu","avi","ankur",True,5,"kaku"]
# for a in my_list:
#     print(a)

# Using a While Loop
# my_list = ["avi","udit","deepak","sonu","avi","ankur",True,5,"kaku"]
# i = 0
# while i<len(my_list):
#     print(my_list[i])
#     i+=1

# List Comprehension --> List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
#employee_list = ["avi","ankur","deepak","anil","akash","rohit","aashu"]
# I want new list employee that have letter 'a'--> Withot List Comprehension
# new_list = []
# for x in employee_list:
#     if "a" in x:
#         new_list.append(x)
# print(new_list)

# With List Comprehension
#new_list1 = [x for x in employee_list if "a" in x]  #  Syntax --> newlist = [expression for item in iterable if condition == True]
#new_list2 = [x.upper() for x in employee_list]
# new_list2 = ["Hello" for x in employee_list]
# print(new_list2)
# print(new_list1)

# Sort Lists --> sort() method that will sort the list alphanumerically, ascending, by default
# employee_list = ["avi","ankur","deepak","anil","akash","rohit","aashu"]
# employee_list.sort()
# print(employee_list)

# To sort descending, use the keyword argument reverse = True
# employee_list.sort(reverse=True)
# print(employee_list)

# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
# employee_list = ["avi","Ankur","deepak","Anil","akash","rohit","Aashu"]
# employee_list.sort()
# print(employee_list)

# Copy a List --> There are ways to make a copy, one way is to use the built-in List method copy().
# employee_list = ["avi","Ankur","deepak","Anil","akash","rohit","Aashu"]
# new_list = employee_list.copy()
# print(new_list)

# Another way to make a copy is to use the built-in method list().
# employee_list = ["avi","Ankur","deepak","Anil","akash","rohit","Aashu"]
# new_list = list(employee_list)
# print(new_list)

# Join Lists --> One of the easiest ways are by using the + operator.
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list3)

# Another way to join two lists is by appending all the items from list2 into list1, one by one
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# for x in list2:
#   list1.append(x)
# print(list1)

# extend() method, where the purpose is to add elements from one list to another list
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# list1.extend(list2)
# print(list1)


# List Methods:-
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list









