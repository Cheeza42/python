#### On this task we made a script that checks if the user's password is valid and strong.

special_characters = "'!@#$%^&*><,;:()?/-_=+" # First we made a varibale that contains alll special characters.

def passwrd_requirements(password): # Here we made variables that are 'False' at the moment. Once we'll putted in the password it will turn 'True'.
      has_upper = False
      has_special = False
      has_digit = False
 
      
      for i in password: # Here we made a loop that will add 1 to the count as long as one of the conditions inside of it: 
      
       if i.isupper(): # If the password contains uppercase it will turn True.
        has_upper = True  
       if (i == special_characters): # If the password contains a special character it will turn True.
        has_special = True
       if i.isdigit(): # If the password contains a digit it will turn True.
        has_digit = True

       return has_upper, has_special, has_digit
password = input("Please enter your password: ") # then we asked the user for a password.

while True:
       has_upper, has_special, has_digit = passwrd_requirements(password) # The loop checks the password according to the function's conditions we made in.
       if len(password) < 8: # We made a condition that says if the password is not long enough it wont proceed.
        print("Invalid password. must contain 8 strings or more..")
       elif not (has_upper, has_special, has_digit):  # If the password do have 8 strings or more but doesnt contain one of the conditions above, the user will get an error massege.
        print("Password must contain an uppercase, a digit and a special character.")   
        password = input("Please try onther password: ")

       if  len(password) == 8: # If the password is 8 strings long, it will recive a weak status.
         print("Password strengh: weak")
     
       elif 8 < len(password) <= 10: # if the pssword is between 8 to 10 strings long, it will recive a medium status.
        print("Password strengh: medium")
         
       elif  len(password) > 10: # If the password is 10 or more strings, it will recive a strong status. 
        print("Password strengh: strong") 
    
   
