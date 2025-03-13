### In this practice we will learn to put up a list of numbers and sum all of them and get an output.

numbers = input("Enter numbers separated by commas: ").split(',') # First we made a variable that ask the user to put a list of numbers using commas to seperete them.
                                                                  # for that we added the '.split()' command that make sure we have a seperator between digits on the list.
numbers = [int(num) for num in numbers] # Second we made the list itself form the input and added a for loop.
print("Sum of numbers:", sum(numbers))  # execute the list and adding a 'sum' command to sum all the numbers on the list.
