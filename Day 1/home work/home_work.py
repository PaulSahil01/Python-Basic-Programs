# program to write hello world
print('Hello World')
# simple program to give student details name, course name, semester number, college name, and city of residence
name = input('who are you? ') # intput one
password = input('password please- ') # input two
# if condition to check credentials
if name == 'Sahil' and password == '123':  
    print('------------------------------------------------\n',name,'\nCyber Security Course\n3rd Semester\nSault College\nResidence of Toronto')
elif password !="123": # elif condition 
    print("wrong password")
# else condition for wrong credentials
else:
    print('wrong username')