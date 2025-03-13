### On this task we learned how to delete files.

import os # First we made an import to get the 'os' function. WHich is the function that responsible for file manegment.

file_name = input("Please enter the file's name that you want to delete: ").strip() # A variable that asks the user to input the folder's name that he want to delete.
insure_del = input(f"Are you sure you want to delete {file_name}? (y/n): ").lower() # Another variable that insure with the user before deleting.

if os.path.exists(file_name): # Here we made a condition. if the code found the file and its exist. it will print the insure massege.
    print(insure_del)

if insure_del == "y": # If the user printed yes("y"), it will delete it withe the 'os.remove' function.
     os.remove(file_name)
     print("Deleting file...") # Display a delete massege.

elif insure_del == "n": # If the user prints no("n"), it will print a cancelation massege. 
    print("Deletion is cancelled.")

else: # Here this 'else' method it for the first condition, if the code havent found the file or was typed wrong.
    print("File not found...")

    