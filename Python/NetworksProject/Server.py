
import socket

def server_program():
    
    host = "10.104.24.218" # get host name
    port = 5000 
    server_socket = socket.socket()  

    #PLEASE NOTE: For some reason the print statements take about 10-20 seconds to load
    server_socket.bind((host, port)) # establish socket with a connection to the host and port number
   #print ('Starting server on', host, port)
   #print ('The Web server URL for this would be http://%s:%d/' % (host, port)) # Use this link to connect

    server_socket.listen(5) # Begin listening on the server for client connections
    c, (client_host, client_port) = server_socket.accept()
    print ('Got connection from', client_host, client_port)
    
    while True:
        # Establish connection with client. 
        data = c.recv(1024).decode()
        if not data: 
            print("Closing...")
            c.close()
            break 
        print("From Client: " + data) # recieve request from client
        message = input(" -> ")
        c.send(message.encode())
 

if __name__ == '__main__':
    server_program()