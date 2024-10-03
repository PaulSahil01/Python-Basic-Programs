# Author of the code: SAHIL PAUL 
# Course : Introduction to Programming
# By submitting this work, I assert that it is my own work and not copied from someone else or from some other source. 
# Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.

# Program to check the salary conversion 
# main function for taking input and salary conversion  
def process_salary():
    # to take input as salary
    salary_input = float(input("Enter your annual salary in euros: "))
    # to take input of country
    country = input("Enter the country to which you want to migrate (Canada, USA, Cambodia, United Kingdom): ")
    # Initialize variables for converted salary and average salary
    salary_conversion = None
    average_salary = None
    # Condition to determine conversion rate and average salary based on the country
    #salary based on canada
    if country == 'Canada':
        salary_conversion = salary_input * 1.50
        average_salary = 56000
    #salary based on USA
    elif country == 'USA':
        salary_conversion = salary_input * 1.10
        average_salary = 45000
    #salary based on cambodia
    elif country == 'Cambodia':
        salary_conversion = salary_input * 4432
        average_salary = 7649856
    #salary based on UK
    elif country == 'United Kingdom':
        salary_conversion = salary_input * 0.85
        average_salary = 45423
    #for invalid input
    else:
        print("Error: Invalid country input.")
        return
    # Condition to check rich in a country
    if salary_conversion > average_salary:
        print("You will be rich in " , country , " with a salary of " , salary_conversion , ".")
    # Condition to check poor in a country
    else:
        print("You will be poor in ", country , " with a salary of " , salary_conversion , ".")
# call the function
process_salary()
