"""
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
Dictionaries are written with curly brackets, and have keys and values.

"""
my_dict = {
    "name":"Avinesh Gautam",
    "company":"Skilline",
    "Designation":"Python Developer",
    "Year":2022,
    "company":"Varnitech OPC"
}
print(my_dict)                              # Output --> {'name': 'Avinesh Gautam', 'company': 'Skilline', 'Designation': 'Python Developer', 'Year': 2022}

# Can referred to by using the key name.
print(my_dict["company"])                   # Output --> Skilline

# Duplicates Not Allowed --> 
# Duplicate values will overwrite existing values.
print(my_dict)                              # {'name': 'Avinesh Gautam', 'company': 'Varnitech OPC', 'Designation': 'Python Developer', 'Year': 2022}

# Dictionary Length
print(len(my_dict))                         # Output --> 4

# The values in dictionary items can be of any data type.
my_dict1 = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(my_dict1)                             # Output --> {'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}

# type()
print(type(my_dict1))                       # <class 'dict'>

# The dict() Constructor.
my_dict2 = dict(name="Avinesh", age=28, company="Google")
print(my_dict2)                             # Output --> {'name': 'Avinesh', 'age': 28, 'company': 'Google'}

# Access Dictionary Items

# get() Method
print(my_dict.get("company"))               # Output --> Varnitech OPC

# The keys() method will return a list of all the keys in the dictionary.
print(my_dict.keys())                       # Output --> dict_keys(['name', 'company', 'Designation', 'Year'])

# Add a new item to the original dictionary, and see that the keys list gets updated as well.
my_dict["salary"] = 9000
print(my_dict)                              # Output --> {'name': 'Avinesh Gautam', 'company': 'Varnitech OPC', 'Designation': 'Python Developer', 'Year': 2022, 'salary': 9000}
print(my_dict.keys())                       # Output --> dict_keys(['name', 'company', 'Designation', 'Year', 'salary'])

# The values() method will return a list of all the values in the dictionary.
print(my_dict.values())                     # Output --> dict_values(['Avinesh Gautam', 'Varnitech OPC', 'Python Developer', 2022, 9000])

# Make a change in the original dictionary, and see that the values list gets updated as well.
my_dict["salary"] = 18000
print(my_dict)                              # Output --> {'name': 'Avinesh Gautam', 'company': 'Varnitech OPC', 'Designation': 'Python Developer', 'Year': 2022, 'salary': 18000}
print(my_dict.values())                     # Output --> dict_values(['Avinesh Gautam', 'Varnitech OPC', 'Python Developer', 2022, 18000])

# The items() method will return each item in a dictionary, as tuples in a list.
print(my_dict.items())                      # Output --> dict_items([('name', 'Avinesh Gautam'), ('company', 'Varnitech OPC'), ('Designation', 'Python Developer'), ('Year', 2022), ('salary', 18000)])

# Check if Key Exists
if "name" in my_dict:
    print("Yes")                            # Output --> Yes

# The update() method will update the dictionary with the items from the given argument.
my_dict.update({"company":"Mind Master"})
print(my_dict)                              # Output --> {'name': 'Avinesh Gautam', 'company': 'Mind Master', 'Designation': 'Python Developer', 'Year': 2022, 'salary': 18000}

# Remove Dictionary Items

# The pop() method removes the item with the specified key name.
my_dict.pop("salary")
print(my_dict)                              # Output --> {'name': 'Avinesh Gautam', 'company': 'Mind Master', 'Designation': 'Python Developer', 'Year': 2022}

# The popitem() method removes the last inserted item.
my_dict.popitem()
print(my_dict)                              # Output --> {'name': 'Avinesh Gautam', 'company': 'Mind Master', 'Designation': 'Python Developer'}

# The del keyword removes the item with the specified key name.
del my_dict["company"]
print(my_dict)                              # Output --> {'name': 'Avinesh Gautam', 'Designation': 'Python Developer'}

# The del keyword can also delete the dictionary completely.
# del my_dict
# print(my_dict)

# The clear() method empties the dictionary.
my_dict.clear()
print(my_dict)                              # Output --> {}

# Loop Dictionaries.

for x in my_dict1:
    print(x)                                # Output --> brand
                                                        # electric
                                                        # year
                                                        # colors

for x in my_dict1.values():
    print(x)

for x in my_dict1.keys():
    print(x)

for x,y in my_dict1.items():
    print(x,y)

# Copy Dictionaries.

# Make a copy of a dictionary with the copy() method.
x = my_dict1.copy()
print(x)                                    # Output --> {'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}

# Make a copy of a dictionary with the dict() function.
x = dict(my_dict1)
print(x)                                    # Output --> {'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}

# Nested Dictionaries.

my_family = {
    "child1" : {
        "name":"Radha",
        "Age":32
    },
    "child2" : {
        "name":"Hemlata",
        "Age":30
    },
    "child3" : {
        "name":"Avinesh",
        "Age":28
    }
}
print(my_family)                            # Output --> {'child1': {'name': 'Radha', 'Age': 32}, 'child2': {'name': 'Hemlata', 'Age': 30}, 'child3': {'name': 'Avinesh', 'Age': 28}}

# Or, if you want to add three dictionaries into a new dictionary.
child1 = {
        "name":"Radha",
        "Age":32
    },
child2 = {
        "name":"Hemlata",
        "Age":30
    },
child3 = {
        "name":"Avinesh",
        "Age":28
    }
my_family = {
    "child1":child1,
    "child2":child2,
    "child3":child3
}
print(my_family)                            # Output --> {'child1': ({'name': 'Radha', 'Age': 32},), 'child2': ({'name': 'Hemlata', 'Age': 30},), 'child3': {'name': 'Avinesh', 'Age': 28}}

# Access Items in Nested Dictionaries.
# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary.
print(my_family["child3"]["name"])          # Output --> Avinesh





