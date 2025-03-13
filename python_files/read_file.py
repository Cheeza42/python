### On this task we will lear to read and print from a file.

with open("C:/Users/AlonE/python/python_files/file1.txt", "r") as file: # First we'll open the file (we'll need to get his path to open it).
   
    content = file.read() # Then we'll make a variable that will read from the file.
    
    print(content) # And in the end we'll print the content inside the file.