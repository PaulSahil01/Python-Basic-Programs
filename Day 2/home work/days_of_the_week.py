# Program to writ Days of the Week
day = int(input("enter number for the = ")) #To take input in number
if day<1 or day>7: # conditon to take numbers  only from 1 to 7 
    print("Error enter a vaild number") # print error message
else : # if elif ladder to print Days of the week
   if day==1:
        print('Monday\n'"it is a weekday")
   elif day==2:
        print('Tuesday\n'"it's a weekday")
   elif day==3:
        print('Wednesday\n'"it's a weekday")
   elif day==4:
        print('Thursday\n'"it's a weekday")
   elif day==5:
        print('Friday\n'"it's a weekday")
   elif day==6:
        print('Saturday\n'"it's a weekend")
   else :
        print('Sunday\n'"it's a weekend")