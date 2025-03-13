### In this practice we will learn how to get the largest number from a list or a tuple

# first we'll ask the user to make al list of numbers at choice.

amoaunt_of_num = int(input("How many numbers doyou want to check?:"))

# then we'll make a list from it

num_list = [amoaunt_of_num]
for i in range(amoaunt_of_num): # We make a loop that the amount of numbers the user putted will be listed
    number = int(input(f"Please insert a number {i+1}:")) # We define the variable 'number' that whatever the user will add.
    num_list.append(number) # Adding the number to the list.

largest = max(num_list) # we made a variable that contains the key 'max()' which finds out the lagest number on the list or in general 
                        # the opposite key to find the smallest one is 'min()' 

print(f"The largest number on the list is: {largest}") # printing the result with the text we added with the format "f"
