"""
A set is a collection which is unordered, unchangeable*, and unindexed.
Set items are unchangeable, but you can remove items and add new items.
Sets are unordered, so you cannot be sure in which order the items will appear.
Sets are written with curly brackets.

"""
my_set1 = {"mango","banana","kiwi",True,5,False}
print(my_set1)

# Duplicates Not Allowed
my_set2 = {1,2,3,4,5,2,3}
print(my_set2)                  # Output --> {1, 2, 3, 4, 5}

# The values True and 1 are considered the same value in sets, and are treated as duplicates.
my_set3 = {"mango","banana","kiwi",True,1,False}
print(my_set3)

# The values False and 0 are considered the same value in sets, and are treated as duplicates
my_set4 = {"mango","banana","kiwi",True,0,False}
print(my_set4)

# Get the Length of a Set
print(len(my_set1))             # Output --> 6
print(type(my_set1))            # Output --> <class 'set'>

# The set() Constructor
my_set5 = set(("apple","banana","kiwi"))        # note the double round-brackets
print(my_set5)

"""
Access Set Items:
You cannot access items in a set by referring to an index or a key.
But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

"""
for x in my_set1:
    print(x)

if "kiwi" in my_set1:
    print("Yes")

# To add one item to a set use the add() method.
my_set1.add("avi")
print(my_set1)

# To add items from another set into the current set, use the update() method.
my_set1.update(my_set2)
print(my_set1)

# update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
x = ["ravi",9]              # List
my_set1.update(x)
print(my_set1)

# Remove Item:
# To remove an item in a set, use the remove()
my_set1.remove("avi")
print(my_set1)
# If the item to remove does not exist, remove() will raise an error.
# my_set1.remove("papaya")
# print(my_set1)

# discard() method
my_set2.discard(5)
print(my_set2)
# If the item to remove does not exist, discard() will NOT raise an error.
my_set3.discard("avi")
print(my_set3)

# pop() method --> This method remove random items so you can not sure which items will removed.
my_set4.pop()
print(my_set4)

# The clear() method empties the set
# my_set1.clear()
# print(my_set1)

# The del keyword will delete the set completely
# del my_set2
# print(my_set2)

# Join Sets:

# The union() and update() methods joins all items from both sets.
# The union() method returns a new set with all items from both sets.
my_set1.union(my_set2)
print(my_set1)

# You can use the | operator instead of the union() method, and you will get the same result.
a = my_set1 | my_set2
print(a)

# Join multiple sets with the union() method:
# set1 = {"a","b","c"}
# set2 = {1,2,3}
# set3 = {True,False}
# set4 = set1.union(set2,set3)
# print(set4)

# When using the | operator, separate the sets with more | operators:
# set1 = {"a","b","c"}
# set2 = {1,2,3}
# set3 = {True,False}
# set4 = set1|set2|set3
# print(set4)

# The union() method allows you to join a set with other data types, like lists or tuples.
# set1 = {"a","b","c"}
# set2 = (1,2,3)
# set3 = set1.union(set2)
# print(set3)

# Note: The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.

# The update() method inserts all items from one set into another.
# Both union() and update() will exclude any duplicate items.
set1 = {"a","b","c"}
set2 = {1,2,3}
set1.update(set2)
print(set1)

# The intersection() method keeps ONLY the duplicates.
# The intersection() method will return a new set, that only contains the items that are present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

# You can use the & operator instead of the intersection() method, and you will get the same result.
# Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)

# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

# You can use the - operator instead of the difference() method, and you will get the same result.
# Note: The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)

# The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

# You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
# Note: The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)

# The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)




