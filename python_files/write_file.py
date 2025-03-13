### Wlcome to python files Operations! here we'll learn the fundementals of files operations.
# First task we learn how to get an input text inside of a file


text = input("Please enter a text to add to the file: ")# At first we'll ask the user for an input.

with open("file1.txt", "w") as file:# And then we'll start the file operation by openning the file ('open()')
# Bounus comment: Python will create the file if its not exsist.
    
# And finally we adding the input into the file.
    file.write(text) 
    

