import ipaddress
# import nmap
import time 


# network_name = [
#     "192.168.0.",  # Replace with your subnet
#     # "10.0.0.0/24",     # Another example subnet
#     # Add more subnets as needed
# ]


<<<<<<< HEAD
for Network in network_name:
    # print(f"\n[+] Scanning subnet: {Network}")
    # # Get the list of IPs to scan
    # ips = list(ipaddress.IPv4Network(Network, strict=False).hosts())
    # print(ips)
    # time.sleep(10)
    defaut = Network
    overall_progress = 0
    for i in range(1, 255):
        ip = defaut + str(i)
        nm = nmap.PortScanner()
        try:
            nm.scan(ip, arguments='-sV -T4')
            if ip in nm.all_hosts():
                host = nm[ip]
                if 'tcp' in host:
                    print(f"\n[+] Open ports on {ip}:")
                    for port in host['tcp']:
                        state = host['tcp'][port]['state']
                        name = host['tcp'][port]['name']
                        product = host['tcp'][port].get('product', '')
                        version = host['tcp'][port].get('version', '')
                        print(f"  {port}/tcp {state} {name} {product} {version}")
        except Exception as e:
            print(f"[-] Error scanning {ip}: {e}")
        overall_progress += 1
        print(f"Current: {defaut}{overall_progress}/254 ")
        time.sleep(0.5)
        # ip_progress.update(1)  # Update IP progress bar
        # print(f"Overall Progress: {overall_progress}/254")
        # print(f"Overall Progress: {overall_progress}/254")
        # print(f"Overall Progress: {overall_progress}/254")    
=======
# for Network in network_name:
#     # print(f"\n[+] Scanning subnet: {Network}")
#     # # Get the list of IPs to scan
#     # ips = list(ipaddress.IPv4Network(Network, strict=False).hosts())
#     # print(ips)
#     # time.sleep(10)
#     defaut = Network
#     overall_progress = 0
#     for i in range(1, 255):
#         ip = defaut + str(i)
#         nm = nmap.PortScanner()
#         try:
#             nm.scan(ip, arguments='-A')
#             if ip in nm.all_hosts():
#                 host = nm[ip]
#                 if 'tcp' in host:
#                     print(f"\n[+] Open ports on {ip}:")
#                     for port in host['tcp']:
#                         state = host['tcp'][port]['state']
#                         name = host['tcp'][port]['name']
#                         product = host['tcp'][port].get('product', '')
#                         version = host['tcp'][port].get('version', '')
#                         print(f"  {port}/tcp {state} {name} {product} {version}")
#         except Exception as e:
#             print(f"[-] Error scanning {ip}: {e}")
#         overall_progress += 1
#         print(f"Current scan on: {defaut}{overall_progress}/254 ")
#         time.sleep(0.5)
#         # ip_progress.update(1)  # Update IP progress bar
#         # print(f"Overall Progress: {overall_progress}/254")
#         # print(f"Overall Progress: {overall_progress}/254")
#         # print(f"Overall Progress: {overall_progress}/254")    


import ipaddress

# Create an IPv4 address
ipv4 = ipaddress.ip_address('192.168.1.1')
print(f"IPv4 Address: {ipv4}")
print(f"Is private: {ipv4.is_private}")
print(f"Packed: {ipv4.packed}")

# Create an IPv4 network
# network = ipaddress.ip_network('192.168.1.0/24')
# print(f"Network: {network}")
# print(f"Number of addresses: {network.num_addresses}")
# print(f"Network address: {network.network_address}")
# print(f"Broadcast address: {network.broadcast_address}")

# Iterate over all hosts in the network
# for host in network.hosts():
#     print(host)
>>>>>>> origin/main
