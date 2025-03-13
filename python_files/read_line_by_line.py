#### On this task we learned to read line by line in our file.

with open("file3.txt", "r") as file:
    for line in file: # here we amde a condition that says for every line in the file, print the line.
        print(line.strip())