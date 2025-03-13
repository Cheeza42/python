### In this script we will learn how to build a calculator via the user inputing.

def calculator(): # (first I have to define a calculator that the script will run under the data I'll put in.) 
    print("Welcone to the calculator!") # (a toping that i added to make it more user-friendly)
calculator() # (thats the define in action! for now it will only prints the greeting massege that I putted in) 
num1 = int(input("Please enter a number:")) # (ask the user to put any number)
op = input("Please enter an operator(+,-,*,/,%):") # (ask the user to put an operator)
num2 = int(input("Please enter another number:")) # (ask the user to complete the drill with anothe number)
    
ops = {'*': num1 * num2, '-': num1 - num2, '+': num1 + num2, '/': num1 / num2 # (those lines contains the definition of each operator, including a condition in the divition operator because we cant divaine in zero)
           if num2 != 0
           else
            "Error: Division by zero is not allowed."}
print(f"The result is: {ops.get(op)}") #(printing the result of the operation with getting the right op definition form the ops key.) 

