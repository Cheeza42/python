#### On this task we've touch the JSON subject which is like a dictionary. 

import json # First we imported the 'json' feature so we can transform our dict into json.
JSON_input = input("Please enter JSON here: ") # Then we asked from the user to write a json.

if not (JSON_input.startswith("{") and JSON_input.endswith("}") and ":" in JSON_input): # Here we made a condition that confirms the user's imput is json
    print("Invalid JSON!")
else:
    print("JSON is valid")

JSON_data = json.loads(JSON_input) # Here we turn our str output into json

if isinstance(JSON_data, dict): # Here we get another condition, thats secures that we actually made the output a json.
   print("JOSN converted successfully! Type: ", type(JSON_data)) # If its succeded we'll get a massege that the type was changed.

keys_number = 0 # We varbialed the number of keys in the json.
values_number = 0 # We varbialed the nuber of values in the json.

for key, value in JSON_data.items(): # Here we made a loop that says for every key/value on the json add +1 to each variable.
   keys_number += 1
   values_number += 1
print(f"Keys: {keys_number} Values: {values_number}") #Display the amount of keys and the amount of values inside the json.