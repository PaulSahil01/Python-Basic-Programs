# Author of the code: SAHIL PAUL 
# Course : Introduction to Programming
# By submitting this work, I assert that it is my own work and not copied from someone else or from some other source. 
# Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.

# Number of steps in the staircase
num = int(input("enter a number= " ))  
# Outer loop for each step
for i in range(1, num + 1):  
    # Inner loop for printing stars
    for j in range(i):  
        print("*", end=" ")  # Print star without moving to a new line
    print()  # Move to the next line after each row
