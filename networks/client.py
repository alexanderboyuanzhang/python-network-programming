import socket
'''AF_INET -> ipv4; SOCK_STREAM -> tcp'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

print("connected to TCP")

full_msg = ''
while(True):
    msg = s.recv(8)
    if len(msg) <= 0:
        break
    full_msg += msg.decode("utf-8")
    print(full_msg)
print(full_msg)
