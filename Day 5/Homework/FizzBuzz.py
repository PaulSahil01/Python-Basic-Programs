# Author of the code: SAHIL PAUL 
# Course : Introduction to Programming
# By submitting this work, I assert that it is my own work and not copied from someone else or from some other source. 
# Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.


# Initialize a variable 'num' to start the loop at 1
num = 1
# Continue the loop as long as 'num' is less than or equal to 50
while num <= 50:
    # Check if 'num' is divisible by both 3 and 5
    if num % 3 == 0 and num % 5 == 0:
        # If true, print "FizzBuzz"
        print("FizzBuzz")
    # Check if 'num' is divisible by 3
    elif num % 3 == 0:
        # If true, print "Fizz"
        print("Fizz")
    # Check if 'num' is divisible by 5
    elif num % 5 == 0:
        # If true, print "Buzz"
        print("Buzz")
    # If none of the above conditions are met
    else:
        # Print the number itself
        print(num)
    # Increment 'num' by 1 to move to the next number
    num += 1

