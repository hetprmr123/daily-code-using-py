#email=xyz123@gmail.com
#password=xyz@123

email = input("enter your email: ")

if '@' in email:
     password = input("enter your password: ")

     if email == "xyz123@gmail.com" and password =="xyz@123":
         print("login successful")
     elif email =="xyz123@gmail.com" and password !="xyz@123":
         print("password is incorrect")
         password = input("enter the correct password:")
         if password == "xyz@123":
          print("this is correct password")
         else:
           print("still password is incorrect")
     else:
       print("login failed")                                                                                                          
else:
 print("enter valid email")
