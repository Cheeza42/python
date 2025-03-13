### On this task we will learn to copy a file's content and place it in another file.

with open ("C:/Users/AlonE/python/python_files/file1.txt", "r") as file: # First we'll open the file that we want to copy from.
    
    content = file.read() # Then we'll make a variable that will read and hold the content inside of it.

with open("file2.txt", "w") as file: # And then we'll make another file with writing premition. 
    
    file.write(content) # At last we'll add the content to the new file using the variable that we made.