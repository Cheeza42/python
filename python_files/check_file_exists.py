#### On this task we want to check if file is exsisting in the system.

import os # So the first step is to import a packege. 'os' is a packege for file system actions.  

file_name = input("Please enter the file's name to check if its exsist: ") # And here we asked from the user to insert a file name.

if os.path.exists(file_name): # Here we made a condition that says if the file's name is exsist print a massege.
    print(f"{file_name} is exsist in the system.")
else: # And if its not print another massege.
    print("file not found.")