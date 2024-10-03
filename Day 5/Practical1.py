# Author of the code: SAHIL PAUL 
# Course : Introduction to Programming
# By submitting this work, I assert that it is my own work and not copied from someone else or from some other source. 
# Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.

#Program to check the correct date 
# To take input in months 
Month = int(input("Enter the month in the numeric form ="))
# To take input in Days
Day = int(input("Enter the day in numeric form ="))
# To take input in Years
Year = int(input("Enter the year in two numeric digits (for example: 98, 20, 21) ="))
# Condition to check the correct month  
if Month <1 or Month >12 :
    # To print Error message
    print("Error!!\nError: Invalid Month Input")
else:
    # Condition to check leap year            
    if Year % 4 == 0:
    # leap year days in different months
     month_days=[31,29,31,30,31,30,31,31,30,31,30,31]
    else:
    # Non leap year days in different months
     month_days=[31,28,31,30,31,30,31,31,30,31,30,31] 
    # Condition to check correct days 
    if Day < 1 or Day > month_days[Month - 1]:
     # To print Error message
     print("Error!!\nError: Invalid Day Input")
    # Condition to check correct year
    elif Year < 0 or Year > 99:
     # To print Error message
     print("Error!!\nError: Invalid Year Input")
    else:
    # printing the correct result
     print("Success: Congratulations! You entered a correct date:",Month,"/",Day,"/",Year)
     
