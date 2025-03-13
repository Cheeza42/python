
with open ("C:/Users/AlonE/python/python_files/server.log", "r") as file:
  
  count = 0
  for line in file:
  
    if "ERROR" in line:
      count += 1

      print(count)