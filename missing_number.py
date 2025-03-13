def num_searcher(): # Making the function to find the missing numbers and fix the list. 
   
    user_input = input("Please enter a list of numbers separated by spaces: ").split() # Making the user to put a list of numbers
    
    num_list = [int(num) for num in user_input] # Making the actual list and turning the strings init into int numbers by using loop.
    
    num_list.sort() # Sorts the list so it can be readble during the solving.

    missing_number = [i for i in range(num_list[0], num_list[-1] + 1) if i not in num_list] 
    # Making a variable that search for the missing number with a for loop and and a condition for what it will do if he finds one.
    
    fixed_list = [i for i in range(num_list[0], num_list[-1] + 1)] # Making the fixed list according to the mistakes the 'missing_number' result.     
    
    if missing_number: # A condition that displays the output if the details inside of the variables are True.
         print(f"the missing number(s): {missing_number}") # Display the missing numbers.
         print(f"Fixed list: {fixed_list}") # Display the fixed list.
    

num_searcher() # Execute the function.

 
 

 

 

 
