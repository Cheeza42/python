### In this practice we'll have 

data = {} # First we made a dictionary that will hold the keys and values. 
keys = [] # Second we made a list that contains the dictionary.


data_range =int(input("Please enter the number of keys you want to write: ")) # Here we made a variable that contain the amount of keys.
for i in range(data_range): 
     key = input(f"Please key(s) {i + 1}: ").strip() # Then we made a loop that get a key from the input
     if key.lower() == "stop": # Here we made a condition that if the user types 'stop' the loop breaks.
       break
     keys.append(key) # Here we made a command that adds keys according to the amount.
for key in keys: #  Then we made another loop that add the value to the right key.
      value = input("Please enter a value: ").strip()
      data[key] = value
    
for key, val in data.items(): # Here we made the third loop that prints for every key its own name and the value.
        print(f"{key}: {val}")

while True: # Then we made a loop that as long the script is valid it will run the other part of the script.
     search_key = input("\nEnter the key you want to search (or type 'stop' to exit search):")
     if search_key == "stop":
          print("Exiting search..")
          break
     if search_key in data: # This final loop execute the specific key search and brings his value.
         print(f"{data[search_key]}") 
           
     
          