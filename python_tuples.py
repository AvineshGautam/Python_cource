"""
A tuple is a collection which is ordered and unchangeable.
Tuple items are ordered, unchangeable, and allow duplicate values.
Tuples are written with round brackets.

"""
my_tuple = ("avinesh","deepak","ankur","mohit","udit")
print(my_tuple)                         # Output --> ('avinesh', 'deepak', 'ankur', 'mohit', 'udit')
print(len(my_tuple))                    # len() fn for length of the tuple Output --> 5


"""
To create a tuple with only one item, you have to add 
a comma after the item, otherwise Python will not recognize it as a tuple.

"""
new_tuple = ("avi",)
print(new_tuple)                        # Output --> ('avi',)
print(type(new_tuple))                  # Output --> <class 'tuple'>
new_tuple1 = ("avi")
print(new_tuple1)                       # Output --> avi but not a tuple
print(type(new_tuple1))                 # Output --> <class 'str'>

# The tuple() Constructor --> It is also possible to use the tuple() constructor to make a tuple.
tuple1 = (("avi",5,True,False,"udit"))  # # note the double round-brackets
print(tuple1)                           # Output --> ('avi', 5, True, False, 'udit')

# Access Tuple Items
print(my_tuple[2])                      # Output --> ankur

# Indexing
print(my_tuple[1:4])                    # Output --> ('deepak', 'ankur', 'mohit')
print(my_tuple[-1:-4:-1])               # Output --> ('udit', 'mohit', 'ankur')
print(my_tuple[:3])                     # Output --> ('avinesh', 'deepak', 'ankur')
print(my_tuple[::2])                    # Output --> ('avinesh', 'ankur', 'udit')
print(my_tuple[2::])                    # Output --> ('ankur', 'mohit', 'udit')
print(my_tuple[::-1])                   # Output --> ('udit', 'mohit', 'ankur', 'deepak', 'avinesh')

# Check if Item Exists --> specified item is present in a tuple use the 'in' keyword
if "udit" in my_tuple:
    print("Yes")                        # Output --> Yes

# Update Tuples --> you cannot change, add, or remove items once the tuple is created
# You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("mango","kiwi","orange",5,True,False,"banana")
# y = list(x)
# y[3] = "papaya"
# x = tuple(y)
# print(x)                                # Output --> ('mango', 'kiwi', 'orange', 'papaya', True, False, 'banana')

# Add Items
# y = list(x)
# y.append("grapes")
# x = tuple(y)
# print(x)                                  # Output --> ('mango', 'kiwi', 'orange', 5, True, False, 'banana', 'grapes')


# Add tuple to a tuple
# y = ("grapes",)
# z = x + y
# print(z)                                # Output --> ('mango', 'kiwi', 'orange', 5, True, False, 'banana', 'grapes')

# Remove Items
# y = list(x)
# y.remove(5)
# x = tuple(y)
# print(x)                                    # Output --> ('mango', 'kiwi', 'orange', True, False, 'banana')

# The del keyword can delete the tuple completely
# del x
# print(x)

"""
Unpack Tuples:
When we create a tuple, we normally assign values to it. This is called "packing" a tuple.
But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking".

"""
employee = ("kishore","avinesh","sonu","mahendra")
# (a,b,c,d) = employee                        # Unpack the tuple
# print(a)                                    # Output --> kishore
# print(b)                                    # Output --> avinesh
# print(c)                                    # Output --> sonu
# print(d)                                    # Output --> mahendra

"""
The number of variables must match the number of values in the tuple, 
if not, you must use an asterisk to collect the remaining values as a list"""
(a,b,*c) = employee
print(a)                                    # Output --> kishore
print(b)                                    # Output --> avinesh
print(c)                                    # Output --> ['sonu', 'mahendra']

# Join Tuples --> To join two or more tuples you can use the + operator
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)                               # Output --> ('a', 'b', 'c', 1, 2, 3)

# Multiply Tuples --> If you want to multiply the content of a tuple a given number of times, you can use the * operator
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)                              # Output --> ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

# Tuple Methods
# count() method --> Syntax -- tuple.count(value)
# thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
# x = thistuple.count(5)
# print(x)                                    # Output --> 2

# Python Tuple index() Method --> Syntax -- tuple.index(value)
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)                                        # Output --> 3 coz it will found first occurence of 8






