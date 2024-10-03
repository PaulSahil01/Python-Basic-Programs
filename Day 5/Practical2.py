# Author of the code: SAHIL PAUL 
# Course : Introduction to Programming
# By submitting this work, I assert that it is my own work and not copied from someone else or from some other source. 
# Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.

#Program to print color combinations
# Globel variables RED Blue Yellow  
RED = "red"
BLUE = "blue"
YELLOW = "yellow"
# To take colour1 input from user
Colour1 = input("Enter the first primary color (red, blue, yellow): ")
# To take Colour2 input from user
Colour2 = input("Enter the second primary color (red, blue, yellow): ")
# Condition to check if colour1 is primary color or not  
if Colour1 not in [RED, BLUE, YELLOW]:
# Error message for invalid input in colour1
 print("Error: Invalid Colour1.")
# Condition to check if Colour2 is primary color or not
elif Colour2 not in [RED, BLUE, YELLOW]:
# Error message for invalid input in Colour2
 print("Error: Invalid Colour2.")
# Condition to check if colour1 and Colour2 are same
elif Colour1 == Colour2:
 print("Error: The two colours you entered are the same.")
else:
# Condition to print the correct color combination as per Primary color RED in colour1 
 if Colour1 == RED:
     # Condition to print the correct color combination as per Primary color BLUE in colour2 
    if Colour2 == BLUE: 
     print("RED + BLUE = PURPLE")
    else :
     print("RED + BLUE = ORANGE")
     # Condition to print the correct color combination as per Primary color BLUE in colour1
 elif Colour1 == BLUE:
     # Condition to print the correct color combination as per Primary color RED in colour2
     if Colour2 == RED: 
      print("BLUE + RED = PURPLE")
     else :
      print("BLUE + YELLOW = GREEN")
      # Condition to print the correct color combination as per Primary color YELLOW in colour1
 elif Colour1 == YELLOW:
     # Condition to print the correct color combination as per Primary color RED is in colour2
     if Colour2 == RED: 
      print("YELLOW + RED = ORANGE")
     else :
      print("YELLOW + BLUE = GREEN")