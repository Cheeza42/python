### As the previous task, now instead of counting lines we'll count words.

with open ("C:/Users/AlonE/python/python_files/file1.txt", "r") as file: # First we'll open the file.

    words = file.read().split() # Then we'll make a variable that will read the file with space scv ('.split()')
    
    count = len(words) # A variable that will count the number of words.
    
    print(count) # prints the number of words.