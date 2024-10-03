# Author of the code: SAHIL PAUL 
# Course : Introduction to Programming
# By submitting this work, I assert that it is my own work and not copied from someone else or from some other source. 
# Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.

# Taking maximum number 
max=int(input("Enter a maximum number: ")) 
# Loop through numbers starting from 1 to the maximum number 
for i in range(1,max+1,1): 
    # If the current number is NOT a multiple of both 5 and 6
    if not (i % 5 == 0 and i % 6 == 0): 
        # Print the number if it's not a multiple of both 5 and 6
        print(i) 

