### On this task we learned how to use another 'try-except' method.

server_name = input("Enter the server name: ") # We asked the user to input a server name. 

try: # Here we use the 'try' method which we might get an error dependes on the user's input.

    if not server_name: # We used here a condition because if the user inputed incorrect info or will not input anything, 'try-except' method will handle it.
       
        raise ValueError("Server name is empty, Please enter a name.") # Here we raised a predictted error that the user didnt input anything.
   
    if not server_name.isalpha():
        
        raise ValueError("Server name must contain only letters.") # Here we raised another predictted error when the user inserted something thats not a letter.

except ValueError as e: # Here we except the error and will print the error according to the error-kind.
 print(f"Error: {e}") # Display an error massege depend on the context.
 
 if server_name: # If there is no problem it will run and else it will write that somthing is wrong.
    print("server is running.")

 else:
    print("Something went wrong.")
