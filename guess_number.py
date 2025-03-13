### On this task we made a guessing game between us and the computer, and we used a new trick!

# At first we used the 'import'. A module which brings in code a feature from external modules such as:  Functions, classes, etc.) 

import random # Here is an example. We brought the feature 'random' from python's library for use in this module. 
import time # And here we did the same with the feature 'time'

def game(): # Here we made a function to contains all the game settings.

     secret_number = random.randint(1, 100) # Here we made a variable that makes the computer to get a random (using the random feature we imported) number from 1 to 100.
     print("Im thinking of a number between 1 to 100...") # Display a massege from the computer to the user.
  
     time.sleep(5) # Here we made a pause between the to masseges from the computer so it will feels more human-like thinking (using the 'time' feature we imported).
     print("All right I got it!") #Display the second massege.

     while True: # Here we made a loop for the game to run as long the input is valid.
        try: # The try method is been used because we might get an error on the way.
         guess_num = int(input("Take a guess: ")) # A variable that asks the user to guess the number.

        except ValueError: # The second part of the try method just incase we'll face an error.
           print("Please enter a valid number: ")
           continue # In each cases we want the loop to continue and not breaks here 
        if guess_num < secret_number: # Here we made a condition that says if the inputed number is smaller, the computer will replay according to the answer.
           print("Too low!")

        elif guess_num > secret_number: # Here we made another condition incase the first one doesnt activated. and will replay according to the answer.
           print("Too high!")
        else: #  And the only option that remains is the the guess was correct.
           print("Congratulations! You guessed right!")
           break # Just after the user will get the right answer the loop will break which means: Game Over!

game() # Execute the function.      
