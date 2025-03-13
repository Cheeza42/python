### On this task we check if strings are anagrams (using the same latters).
word1 = input("Please enter a strig: ") # Ask an input from the user.
word2 = input("Please enter the second string: ") # Ask an input from the user.

if sorted(word1) == sorted(word2): # Here we made a condition, that if the sorted latters on word1 equels the same latters in word2 we get a match.
    print("Those strings are anagrams!") # Display a massege that confims the condition is met.
else:
    print("The strings arent anagrams..") # Display a massege that confirms the condition isnt met