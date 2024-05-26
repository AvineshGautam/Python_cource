"""
A for loop is used for iterating over a sequence 
(that is either a list, a tuple, a dictionary, a set, or a string).

"""
employee = ["avi","kishore","sonu","akhil","mahendra"]
for x in employee:
    print(x)

# Looping Through a String.
for x in "Avinesh":
    print(x)

# The break Statement:
# With the break statement we can stop the loop before it has looped through all the items:
employee = ["avi","kishore","sonu","akhil","mahendra"]
for x in employee:
    print(x)                                            # Output --> avi kishore sonu akhil
    if x == "akhil":
        break

# but this time the break comes before the print:
employee = ["avi","kishore","sonu","akhil","mahendra"]
for x in employee:
    if x == "akhil":
        break
    print(x)                                            # Output --> avi kishore sonu

# The continue Statement:
# With the continue statement we can stop the current iteration of the loop, and continue with the next:
employee = ["avi","kishore","sonu","akhil","mahendra"]
for x in employee:
    if x == "akhil":
        continue
    print(x)                                            # Output --> avi kishore sonu mahendra

# The range() Function:
"""
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 
(by default), and ends at a specified number.

"""
for x in range(3):
    print(x)                                            # Output --> 0 1 2

for x in range(1,5):
    print(x)                                            # Output --> 1 2 3 4

for x in range(1,20,3):
    print(x)                                            # Output --> 1 4 7 10 13 16 19

# Else in For Loop:
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(5):
    print(x)
else:
    print("Loop Finished !")                            # Output --> 0 1 2 3 4 Loop Finished !

# Note: The else block will NOT be executed if the loop is stopped by a break statement.
for x in range(5):
    if x == 3:
        break
    print(x)
else:
    print("Loop Finished !")                            # Output --> 0 1 2


# Nested Loops --> A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":
employee = ["avi","kishore","sonu","akhil","mahendra"]
salary = [10000, 20000, 30000, 40000, 50000]
for x in employee:
    for y in salary:
        print(x, y)
"""
Output:
avi 10000
avi 20000
avi 30000
avi 40000
avi 50000
kishore 10000
kishore 20000
kishore 30000
kishore 40000
kishore 50000
sonu 10000
sonu 20000
sonu 30000
sonu 40000
sonu 50000
akhil 10000
akhil 20000
akhil 30000
akhil 40000
akhil 50000
mahendra 10000
mahendra 20000
mahendra 30000
mahendra 40000
mahendra 50000

"""

# The pass Statement:
# for loops cannot be empty, but if you for some reason have a for loop with no content, 
# put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass