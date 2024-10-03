# Author of the code: SAHIL PAUL 
# Course : Introduction to Programming
# By submitting this work, I assert that it is my own work and not copied from someone else or from some other source. 
# Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.


# Define a list of employees
employee_list = [  
    (1001, "Alice Smith", "Finance"),
    (1002, "Bob Johnson", "IT"),
    (1003, "Carol Davis", "HR")
]

# Create a new employee tuple
new_employee = (1004, "David Wilson", "Marketing")  
# Add the new employee to the list
employee_list.append(new_employee)  

# Print the entire employee list before removal
print("\nEmployee List before Removal:")  
for emp in employee_list:  
    # Print each employee's details
    print(f"ID: {emp[0]}, Name: {emp[1]}, Department: {emp[2]}")  

# Remove the last employee from the list
removed_employee = employee_list.pop()  
# Print the removed employee's details
print(f"\nRemoved Employee: ID: {removed_employee[0]}, Name: {removed_employee[1]}, Department: {removed_employee[2]}")  

# Print the entire employee list after removal
print("\nFinal Employee List:")  
for emp in employee_list:  
    # Print each employee's details
    print(f"ID: {emp[0]}, Name: {emp[1]}, Department: {emp[2]}")  

