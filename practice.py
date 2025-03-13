
amount_of_services = 3

servers = []

for i in range(amount_of_services):
    servers.append(input(f"Please enter a server name here{i+1}:"))
    print(servers)


server_ips = {}
for server in servers:
    ip_address = input(f"Please enter the current IP address for {server}:")
    server_ips[server] = ip_address
    print(server_ips)

while True:
    server_name = input("Please insert the server name to view its details:")
    
    if server_name in server_ips:
   
     print(f"{server_name} is available in {server_ips[server_name]} .") 
    
    else: 

     print(f"Oops. {server_name} not found, please try again.")

    update_ip = input("Do you want to update server? yes/no:")

    if update_ip == "yes":

       server_name = input("Please insert the server name that you want to be changed:")
       new_ip = input("Please enter the new ip:")

       if server_name in server_ips:
        server_ips[server_name] = new_ip

       else: 
          print("Your action has been cancelled.") 
    
    else:
       print(server_ips)
