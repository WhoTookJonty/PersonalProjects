#TO SEARCH FOR PACKETS IN WIRESHARK: tcp.port == 5000 || udp.port == 5000
#use above filter in filter bar. 
import socket
def client_program():
    host = "10.104.24.218"  #Include IP of target sever as hostname (found through local WiFi IPv4 adress - ipconfig in cmd prompt)
    port = 5000  #no need to change this
    client_socket = socket.socket()  
    client_socket.connect((host, port))  
    
    message = input(" -> ")  #when you see arrow on command line: connection is estabalished and you can now send messages.
    
    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()  
        print('Received from server: ' + data)  
        message = input(" -> ")  
   
    client_socket.close()  
if __name__ == '__main__':
    client_program()