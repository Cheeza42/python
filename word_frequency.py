### In this practice we will learn the get the frequency for words in dictionaries.
sentence = input("Please enter a sentence here: ") # First we'll make a sentense based on the user's input.

words = sentence.split() # Second we made a variable for the words un the sentence by using '.split()' that splits the sentence into words

word_count = {} # Then we made a dictionary for the frequency 

for word in words: # After that we made a loop that contains:

    word_count[word] = word_count.get(word, 0) + 1

    # the method '.get()' is for getting the words and the number of time they appears(if they not appear it will bring us the number 0)
    # '+1' for updating the counting words

print("\nWord frequency count:") # Prints the output and with the '\n' it will print it with extra spaces between the lines
for word, count in word_count.items(): # In the end we added a loop that prints an output for every word and the amount of times it appears in the dictionary
        print(f"{word}:{count}")