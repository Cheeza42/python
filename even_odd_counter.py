### In this task we want to counter an even and odd numbers based on the user's input.


def main(): # First we define a main function that will contain the counter actions.
    
    num_counter = input("Please enter numbers to the list : ") # Second we made a list that will contain the numbers.
    
    try: # In here we used 'try' opreration that will try to execute the script that might get us an error.
       
        numbers = [int(num) for num in num_counter.split()] # The list itself that will contains a loop and have to get a space between the numbers by using '.split()'.
    
    
    except ValueError: # Here is the sulotion for 'try' incase python finds an erorr in the code called 'except' and using ValueError to deal with it.
     print("Please enter only int numbers.") 
     return

    even_count = 0 # We made a variable which represents the start point of counting the even numbers.
    odd_count = 0 # Then we made a variable which represents the start point of counting the odd numbers.
    
    for num in numbers: # Here we made a loop for the counting with a condition: 
       if num % 2 ==0: # If the numbers are even they will be counted as even and will get in the even_count variable.
          even_count += 1
       else: # Any other result (odd numbers) will be counted as an odd and will get in the odd_count variable.
          odd_count += 1

    print("Even numbers count:", even_count) # Display the result.
    print("Odd numbers are:", odd_count) # Display the other result.

main() # Execute the function.