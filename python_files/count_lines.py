# On this task we will learn how to count the number of lines in two ways:

# First way is to open the file at the beginning.
with open ("C:/Users/AlonE/python/python_files/file1.txt", "r") as file:
# Then we'll make a varibale for the counting startpoint.
 count = 0
# And then we'll make a loop that will add every line in the file to the count. 
 for line in file:
    
    count += 1
#And finally we'll print the amount of lines.
print(count)

"----------------------------------------------"
# The second way is more cleaner and simple:
# First we'll open the file:
with open ("C:/Users/AlonE/python/python_files/file1.txt") as file:
# Then we'll make a variable that will make a list of lines from the file
  lines = file.readlines() 
# Then we count the mount of lines that we get from the listed lines
  count = len(lines)
  # Print the number of line that the file contain.
  print(count)