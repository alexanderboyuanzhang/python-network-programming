import socket
'''AF_INET -> ipv4; SOCK_STREAM -> tcp'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
'''our host, and port 1234 '''
s.bind((socket.gethostname(), 1234))
''' the server leaves a queue of 5 '''
s.listen(5)

''' listen forever, and accept anybody that connects '''
while(True):
    '''the object will be saved in clientsocket, the ip address will be saved in address '''
    clientsocket, address = s.accept()
    print("connection from ", address, " has been established!")
    ''' send information to the clientsocket '''
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    clientsocket.close()
