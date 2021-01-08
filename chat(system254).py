import socket
import os
import threading

os.system("clear")

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = "192.168.43.224"
port = 8888
server.bind((ip,port))


def sender():
  data = ""
  client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  #server_ip = "192.168.43.165"
  
  os.system("tput setaf 3")
  print("Enter the Server IP : ")
  os.system("tput setaf 7")
  server_ip = input()
  server_port = 8188
  os.system("tput setaf 3")
  print("Enter your name : ")
  os.system("tput setaf 7")
  name = input()
  os.system("tput setaf 4")
  print("\nReaching port 8188........")
  os.system("sleep 1")
  print("Connected\n")
  os.system("tput setaf 7")
  print("Joined in as %s" %name)
  print()
  os.system("tput setaf 1")
  print(" CHAT \n")
  os.system("tput setaf 7")
  while True:
    if "Bye" in data or "bye" in data or "Exit" in data or "exit" in data:
      os.system("tput setaf 1")
      print("\nClosed\n")
      os.system("tput setaf 7")
      os._exit(1)
    #print("> ",end="")
    data = input()
    
    final_data = "> " + name + " : " + data
    client.sendto(final_data.encode() , (server_ip, server_port ) )

def receiver():
  while True:
    x = server.recvfrom(1024)
    clientIP = x[1][0]

    os.system("tput setaf 6")
    print(x[0].decode())
    os.system("tput setaf 7")
    

send = threading.Thread( target = sender )
recv = threading.Thread( target = receiver )

send.start()
recv.start()



