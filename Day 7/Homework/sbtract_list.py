# Author of the code: SAHIL PAUL 
# Course : Introduction to Programming
# By submitting this work, I assert that it is my own work and not copied from someone else or from some other source. 
# Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.

# Function to subtract two lists
def subtract_lists(list1,list2):
 # Check if both lists are of equal size
 if len(list1)==len(list2):
  # Initialize an empty list to store the results
  subtracted_list=[]
  # Iterate through the indices of the lists
  for i in range(len(list1)):
   # Subtract the corresponding elements of list1 from list2
   subtracted_value=list2[i]-list1[i]
   # Append the result to the subtracted_list
   subtracted_list.append(subtracted_value)
  # Return the list of subtracted values
  return subtracted_list
 else:
  # Print a message if the lists are not equal in size
  print("The lists are not equal in size.")
  # Return an empty list
  return []
# Initialize list1 with values
list1=[23,20,75]
# Initialize list2 with values
list2=[76,50,30]
# Call the function and store the result
result=subtract_lists(list1,list2)
# Print the resulting list after subtraction
print("Resulting list after subtraction:",result)
