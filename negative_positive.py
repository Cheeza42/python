### In this practice we will insert a number by the user's chocie, and whatever the number is, the script will detected if its a positive or negative number.

num = int(input("Please enter a number:")) # first we'll make a variable that ask the user to insert a number.

if num > 0: #we made a condition, that says if the user's number bigger then 0 it will replay an costumed output.
    print("Your number is positive.")

elif num < 0: # we made another condition that says if the first condition does not acttivated, execute another option which is when the user's number smaller then 0.
     print("Your number negative.")
else: #and this is the output we will recive for any other options that dont have a condition to it.
        print("Your number is equal to zero.")



    