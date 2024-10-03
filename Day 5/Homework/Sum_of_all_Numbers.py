# Author of the code: SAHIL PAUL 
# Course : Introduction to Programming
# By submitting this work, I assert that it is my own work and not copied from someone else or from some other source. 
# Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.

# Accepts a number from the user and converts it to an integer
num=int(input("Enter a number :"))
# Initializes a variable 'sum' to store the cumulative sum
sum=0
# Loops from 1 to the given number (inclusive) with a step of 1
for i in range(1,num+1,1):
    # Adds the current value of 'i' to 'sum' in each iteration
    sum+=i
# Prints the final sum of all numbers from 1 to the entered number
print(f"The sum of all numbers from 1 to {num} is =",sum)

    