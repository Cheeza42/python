### On this task we used tuples which is immuteble lists.

def tuple_basics(): # First we made a function for multiple actions in this script.

    user_input = input("For creating a tuple, please insert numbers: ") # Then we made a variable that ask the user to insert numbers for the tuple.
 
    numbers = [int(x) for x in user_input.split()] # Then we made a variable that contains a list in it which will becaome our tuple eventualy.

    final_tuple = tuple(numbers) # This this the final tuple that will get the numbers for it from the previous variable.
    print("Tuple result:",final_tuple) # Displays the final result of the tuple.
    print(f"Max number is:{max(final_tuple)}") # Displays the max number from it.
    print(f"Min number is:{min(final_tuple)}") # Displays the min nunmber from it.
    print(f"The sum is:{sum(final_tuple)}") # Dsiplays the sum of the number i the tuple.

tuple_basics() # Executes the funtion.