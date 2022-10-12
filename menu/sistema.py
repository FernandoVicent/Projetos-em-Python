import socket
import os

def get_Host_name_IP():
    try:
        host_name = input("qual o host que quer procurar")
        host_ip = socket.gethostbyname(host_name)
        print("Hostname :  ",host_name)
        print("IP : ",host_ip)
        user = os.getlogin()
        print(user)
    except:
        print("Unable to get Hostname and IP")
get_Host_name_IP()

# using environ.get() method getting
# current username
us = os.environ.get('PROD171056')
print(us)