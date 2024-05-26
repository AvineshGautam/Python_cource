"""
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.

"""
# Creating a Function:-> In Python a function is defined using the def keyword.
# Calling a Function
def my_fn():
    print("Hello World !")
my_fn()                                     # Output --> Hello World !

# Arguments:
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
def my_fn(f_name,l_name):
    print(f_name + " " + l_name + " " + "My Full Name")
my_fn("Avinesh", "Gautam")                  # Output --> Avinesh Gautam My Full Name
my_fn("Ankur", "Yadav")
my_fn("Deepak", "Kumar")                               # Ankur Yadav My Full Name
                                                       # Deepak Kumar My Full Name

# Parameters or Arguments?
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

# Arbitrary Arguments, *args
"""
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:

"""
def my_fn(*employee):
    print("Our Emploee is", employee[2])
my_fn("Avi","Ankur","Deepak","Udit")                # Output --> Our Emploee is Deepak

def my_function(*args):
    for arg in args:
        print(arg)

# Calling the function with different numbers of arguments
my_function(1, 2, 3)
my_function("apple", "banana", "cherry")


# Keyword Arguments:
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.
def my_fn(employee2, employee3, employee4, employee1):
    print("Most Senior Employee Is", employee2)
my_fn(employee1="Avi", employee2="Deepak", employee3="Ankur", employee4="Udit")         # Output --> Most Senior Employee Is Deepak

# Arbitrary Keyword Arguments, **kwargs
"""
**kwargs is used to pass a variable number of keyword arguments to a function. 
It allows you to pass any number of keyword arguments, which are then accessible as a dictionary.

"""
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function with different keyword arguments
my_function(name="Alice", age=30, city="New York")
my_function(fruit="apple", color="red", price=1.2)

# Default Parameter Value:
# If we call the function without argument, it uses the default value.
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Passing a List as an Argument:
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
def my_fn(employee):
    for x in employee:
        print(x)
my_list = ["avi","kishore","sonu"]
my_fn(my_list)

# Return Values:
# To let a function return a value, use the return statement:
def my_fn(x):
    return x * 5
print(my_fn(5))
print(my_fn(10))


# The pass Statement: Function is not empty for some reasons it will empty use pass statement to avoid error.
def my_fn():
    pass

# Recursion:
# In simple words, it is a process in which a function calls itself directly or indirectly. 
# Recursive function                            
def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))                                     # Output --> 120


