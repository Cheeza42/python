import json

JSON_input = input("Please enter JSON here: ")

print("Type before conversion:", type(JSON_input))

JSON_data = json.loads(JSON_input)

print("Type after conversion:", type(JSON_data))