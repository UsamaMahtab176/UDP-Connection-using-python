import socket
import time
import pickle

HEADERSIZE = 10



s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
     clientsocket, address = s.accept()
     print(f"Connection from {address} has been estalished!")

     d = {1: "Hey" , 2: "There"}
     msg =  pickle.dumps(d)
    
     msg = bytes(f'{len(msg):^{HEADERSIZE}}' , "utf-8")+ msg
     clientsocket.send(msg)
    





























# HEADERSIZE = 10

# s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((socket.gethostname(), 1234))
# s.listen(5)

# while True:
#     clientsocket, address = s.accept()
#     print(f"Connection from {address} has been estalished!")

#     msg = "Welcome to the server!"
#     msg = f'{len(msg):^{HEADERSIZE}}'+ msg
#     clientsocket.send(bytes(msg, "utf-8"))
    
#     while True:
#             time.sleep(3)
#             msg = f"the time is! {time.time()}"
#             msg = f'{len(msg):<{HEADERSIZE}}'+ msg
#             clientsocket.send(bytes(msg, "utf-8"))
    


    