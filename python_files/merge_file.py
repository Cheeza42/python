### On this task we learned how to merge two files's content into one file.

with open("file1.txt", "r") as file1, open("file2.txt", "r") as file2: # First we called to the files that we want to take the content from.
    content1 = file1.read() # Varibale that holds the content from file1.
    content2 = file2.read() # Variable that holds the content from file2.

    content3 = content1 + "\n" + content2 # Here we made the variable that contains the merged content.

    with open("file4.txt", "w") as file4: # And here we made the new file and we added the new merged content.
        file4.write(content3)
    
    