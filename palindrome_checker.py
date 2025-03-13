### In this task we made a function that will check for palindrome words.

def palindrome_checker(): # First we will define the function. 
   
    while True: # Then we will made a 'while' loop that will go as long it doesnt ordered to break.

         user_input = input("plaese write a word(or type 'exit' to quit): ") # A variable that ask the user to enter a string.
         
         if user_input == "exit": # A condition that says if the user want to quit the loop he'll have to write 'exit'.
            print("Alright then, goodbye..")
            break

         if user_input == user_input[::-1]: # Here we made a condition that if the string equals to himself when it written backwards it will display us a massege according to the data it has.
           print("Thats right! this word is palindrome!") # Display a massege that the word is palindrome.
           break # When the user is correct the loop will break.
         else: # The other options are when the user failed and will send him to enter another word or quit by type 'exit'.
          print("Sorry, that isnt palindrome.") # Display a fail massege.
         

palindrome_checker() # Execute the function.