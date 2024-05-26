"""
With the while loop we can execute a set of statements as long as a condition is true.

"""
x = 1
while x<=5:
    print(x)
    x+=1                                                # Output --> 1,2,3,4,5

# Note: remember to increment i, or else the loop will continue forever.
# x = 1
# while x<=5:
#     print(x)

# The break Statement:
# With the break statement we can stop the loop even if the while condition is true:
x = 1
while x<5:
    print(x)
    if x == 4:
        break
    x+=1                                                # Output --> 1,2,3,4

# The continue Statement:
# With the continue statement we can stop the current iteration, and continue with the next:
x = 0
while x < 10:
    x+=1
    if x == 6:
        continue
    print(x)                                            # Output --> 1,2,3,4,5,7,8,9,10
                                                        # Note - 6 is missing

# The else Statement:
# With the else statement we can run a block of code once when the condition no longer is true:
# Print a message once the condition is false:
x = 0
while x<5:
    print(x)
    x+=1                                                
else:
    print("No longer used")