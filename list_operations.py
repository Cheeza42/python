### In this practice we will make a list and use it for multipule actions.

numbers = input("Please insert numbers to create list: ").split(',') # First we created an input that will made the list by user's choice. 

numbers = [float(num) for num in numbers] # Second we made the list itself that contains the input we asked the user in a loop.

total_sum = sum(numbers) #Then we made a variable that contains the sum of the numbers of the list.
average = total_sum / len(numbers) if len(numbers) > 0 else 0 # After that we made a variable that contains:
# The total sum of the numbers
# The length of the list.
# A condition to get the average number of the list by devine the sum of the numbers in the length of the list.

print(f"Sum: {total_sum}") #Exectue the sum of the list.
print(f"Average: {average:.2f}") #Execute the average of the list.

print(f"Largest number: {max(numbers)}") # Brings the largest number of the list.
print(f"Smallest number: {min(numbers)}") #Brings the smallest number of the list.

print(numbers[::-1]) #Prints the list in reverse.