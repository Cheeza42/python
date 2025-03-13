#### In this task we learnd to get a prime number out of a script.


import math # First we imported the 'math' method for use later on.

def prime_checker(): # Then we made a function that willrun the calculation. 

 num_input = int(input("Please insert a number: ")) # We made a variable that ask the user for interger number.
 if num_input < 2: # Then we made the first condition, that if the number is less then 2 it will return a error massege. 
     print("This number isnt a prime number..")
     return   # The return part will finish the function.
 
 for num in range(2, int(math.sqrt(num_input)) + 1): #Here we made a 'for' loop that calculate with the help of 'math' method to see if it a prime number or not.
        # Bounus commnet: we used 'math.sqrt' to get the square number of the input number in our 'range' 
   
        if num_input % num == 0: # The second codition says if the number isnt prime it will return a fail massege.
          print("This number isnt a prime number..")
          return #This return is the same as we used him before. It will end the function.
        # Bounus comment: If we'll use 'return' there is no need to use 'else' because the computer recognize the number isnt prime
        print("Well done. This is a prime number!") # And here its the display we will get if the number is prime.

prime_checker() # Executes the function.