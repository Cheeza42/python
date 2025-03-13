### In this task we made a function that will run the famous Fabonacci's sequence.

n = int(input("Please enter a number: ")) # First we made a variable that will ask a number from the user(this number will be our range for the sequence.)
def fabonacci_gen(n): # And here we made the function itself that runs with the 'n' variable
    
    a, b = 0, 1 # Here we made the first numbers that starts the Fabonacci's sequence which is 0, 1.

    for _ in range(n): # Here we made a 'for' loop in range of the input number. 
                       # Bounus commnet: the underscore represents no index beacuse we dont need one.
        print(a, end=" ") # Dsiplay the numbers that will be printed in the loop.
                          # Bounus commnet: The 'end=' feature will make spaces between the numbers in the same line instead of new lines.
        a,b = b, a + b # The Fabonacci's sequence itself as a variable. 

fabonacci_gen(n) # Executes the function.
