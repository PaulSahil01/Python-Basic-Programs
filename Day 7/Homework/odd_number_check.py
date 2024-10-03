# Author of the code: SAHIL PAUL 
# Course : Introduction to Programming
# By submitting this work, I assert that it is my own work and not copied from someone else or from some other source. 
# Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.

# Get lower and upper limits from the user
lower = int(input("Enter the lower limit: "))  # User inputs the lower limit
upper = int(input("Enter the upper limit: "))  # User inputs the upper limit

# Create a list from lower limit to upper limit (inclusive)
myList = list(range(lower, upper + 1))

# Display a message for the user
print("Odd numbers in the list are:")

# Iterate through the list to find odd numbers
for number in myList:
    if number % 2 != 0:  # Check if the number is odd
        print(number)  # Display the odd number

