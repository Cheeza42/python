### In this practice we will learn how to make an even/odd script

a = input("Please enter a number:") #(ask the user to input a number of choosing)
b = input("Please enter another number:" ) #(ask the user to input another number of choosing)
result = int(a + b) #(calculate the result between the inputed numbers of the user)
if result % 2 == 0: #(we added a condition! that the residue of the result is even we'll get adjusted output)
    print("the number is even") #(this is the adjusted output in case the condition is fulfilled)
else: #(this is the other option/s incase the condition isnt fulfilled)
   print("the number is odd") #(an output that we chose incase the condition isn't fulfilled)
