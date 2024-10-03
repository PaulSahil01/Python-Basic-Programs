# Author of the code: SAHIL PAUL 
# Course : Introduction to Programming
# By submitting this work, I assert that it is my own work and not copied from someone else or from some other source. 
# Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.

# Declare and initialize the tuple
myTuple = (10, 20, 30, 40, 50)

# Take an element input from the user
element = int(input("Enter an element to check: "))

# Check if the element exists in the tuple
if element in myTuple:
    # Find the position of the element (index)
    position = myTuple.index(element)
    # Print the element and its position
    print(f"Element {element} exists at position: {position}")
else:
    # Display error message
    print("Element does not exist.")
