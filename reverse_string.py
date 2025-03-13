### In this practice we will learn how to make an reverse output

for numbers in range(10, 0, -1): # first we made a loop with the 'range()' command.  
# range([10]start-point, [0]stop-point, [-1]the step between the start and stop points)'
# The negative sign in the step will make the step between the numbers in reverse
     print(numbers) #execute the script

### now lets make a string that will be reversed after executing

def reverse_string(): #first we'll define a variable that contains the command

    user_input = input("Enter a string:") # Then we'll make an user's input
    print("reversed string:", user_input[::-1]) 
    # Last thing is to make a print command using the string that inputted with the same methods we used in numbers.
    # for strings we dont have a start or stop placements but we want it to be read in reverse so we used the step method which is -1

reverse_string() # Execute the define