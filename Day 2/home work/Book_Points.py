# Points Stystem program for Books
P = int(0)
Number_of_books =int(input("Number of book purchased = "))
if  Number_of_books<=5:
    print('Total number of books purchases=',Number_of_books)
    P=20 
elif  Number_of_books>=6 and Number_of_books<=10:
    print('Total number of books purchases=',Number_of_books,)
    P=40
else:
    print('Total number of books purchases=',Number_of_books,)
    P=100
        
