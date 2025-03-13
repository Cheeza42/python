### In this task we made two different sets and made couple of executes with them.  


def set_operation(): # At first we define the set operation function.
    set1_input = input("Please create a set by inserting numbers here: ") # Then we made a variable that will contain the set afterwards.
    set1 = set([int(x) for x in set1_input.split()]) # And here we made the set itself that contains a loop that fills the set and require a space between each number  

    set2_input = input("please create the second set: ") # Here we made the 2nd variable for the ither set.
    set2 = set([int(x) for x in set2_input.split()]) # And here we made the 2nd set that contains the same loop the 1st set has. 
    
    print("Union:", set1 | set2) # Displays the union between the two sets.
    print("intersection:", set1 & set2) # Displays the intersection between the sets.
    print("difference:", set1 - set2) # Display the difference between the sets.

set_operation() # Executes the function.



