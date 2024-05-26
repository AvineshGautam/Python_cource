"""
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

"""
a = 10
b = 5
if a>b:
    print("Yes")                                # Output --> Yes

# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

a = 5
b = 5
if a>b:
    print("a is greater than b")
elif a==b:
    print("a is equal to b")                    # Output --> a is equal to b

# The else keyword catches anything which isn't caught by the preceding conditions.

a = 12
b = 14
if a>b:
    print("a is greater than b")
elif a==b:
    print("a is equal to b")
else:
    print("a is less than b")                   # Output --> a is less than b

# One line if statement:
a = 10
b = 5
if a>b: print("a is greater than b")            # Output --> a is greater than b

# One line if else statement:
# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line.
a = 25
b = 21
print("a is greater than b") if a>b else print("a is not greater than b")       # Output --> a is greater than b

# You can also have multiple else statements on the same line.
a = 12
b = 12
print("a is greater than b") if a>b else print("a is equal b") if a==b else print("a is less than b")           # Output --> a is equal b

# The and keyword is a logical operator, and is used to combine conditional statements.
a = 6
b = 10
c = 8
if a<b and b>c:
    print("True")                               # Output --> True
else:
    print("False")

# The or keyword is a logical operator, and is used to combine conditional statements.

a = 6
b = 10
c = 8
if a<b or b<c:
    print("Atleast one condition should be True")       # Output --> Atleast one condition should be True

# The not keyword is a logical operator, and is used to reverse the result of the conditional statement.
a = 6
b = 10
if not a>b:
    print("a is less than b")                           # Output --> a is less than b

# Nested If --> You can have if statements inside if statements, this is called nested if statements.
a = 20
if a>5:
    print("Yes")
    if a>10:
        print("Yes")                                    # Output --> Yes
        if a>15:                                                    # Yes
            print("Yes")                                            # Yes
    else:
        print("False")      

# The pass Statement:
# if statements cannot be empty, but if you for some reason have an 
# if statement with no content, put in the pass statement to avoid getting an error.  
a = 10
b = 5
if a>b:
    pass                       