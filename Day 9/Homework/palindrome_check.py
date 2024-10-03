# Author of the code: SAHIL PAUL 
# Course : Introduction to Programming
# By submitting this work, I assert that it is my own work and not copied from someone else or from some other source. 
# Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.

# Take a string input from the user
myString = input("Enter a string: ")

# Convert the string to uppercase
print("Uppercase:", myString.upper())

# Find the length of the string
print("Length:", len(myString))

# Reverse the string
reversed_string = myString[::-1]
print("Reversed:", reversed_string)

# Check if the string is a palindrome and print the message
if myString == reversed_string:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

