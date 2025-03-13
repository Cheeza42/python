#### In this practice we will learn to convert Celsius to Fahrenheit and vice versa. 
def celsius_to_fahrenheit(celsius): # First we define a function that will contain the calculation of Celsius. 
    return (celsius * 9/5) + 32
def celsius_to_fahrenheit(fahrenheit): # Second we define another funtion that will contain the calculation of Fahrenheit.
    return (fahrenheit - 32) * 5/9

choice = input("Convert (C)elsius to (F)ahrenheit or (F)ahrenheit to (C)elsius? (C/F):").strip() # Then we made an input order fo the user to choose the convertation (C/F).

if choice == "C": # And then we made a condition that making the covertation between Celsius to Fahrenheit.
   celsius = float(input("Enter temperature in Celsius: "))
   fahrenheit = celsius_to_fahrenheit(celsius)
   print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

elif choice == "F": # And then we made another condition that execute when the previous condition was false.
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = celsius_to_fahrenheit(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

else: # And if someone will enter wrong key the script will respond an error massege. 
    print("Invalid choise! Please enter 'C' or 'F' .") 