### Here we got a simple task to create a file with a defualt content in it.

with open("file3.txt", "w") as file: # First we'll start with the 'with open()' function that creates the file if its not exists.
    
    file.write("Heelo World Again.") # Then we'll use 'file.wirte()' and write inside of it the text that we want.
    
    print(file) # The printing method fills the file with the content we worte in the 'file.write' as the default content.