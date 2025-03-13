### On this task we learned how to encrypt a file with 'Ceaser Chiper' encrypt, and decrypt a file
# Bounus Comment: IN 'Ceasar Cipher' encrypt every letter shifting forword based on the shifting number.

with open("input.txt", "w") as file: # First we made a file in first place and worte some text in it
    file.write("Hello world")


shift = 3 # Here we made a variable that contains the shifting number

with open("input.txt", "r") as file: # Now we open again the file but now on 'readmode'.
    text = file.read() # This variable reads the content in the file.

    encrypted_text = "" # The variable that will hold the encrypted massege.
                        # Bounus comment: we used "" here as we use on a list[] or dict {} to store init the strings

for char in text : # Here e made a loop that will activate the Ceasar Cipher's encrypt:
    encrypted_char = chr(ord(char) + shift) 
    # First 'ord()' turn the letter into a ASCII number.
    # Next the 'shift' variable add the shifting number to the current number.
    # And finally 'chr()' turns the number into a letter again.
      
    encrypted_text += encrypted_char # And here we made our 'code' into a variable.

print(encrypted_text) # Display the 'code' that we made.
