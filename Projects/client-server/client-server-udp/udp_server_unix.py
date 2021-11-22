import os
import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
unix_file_name = 'unix.sock'

if os.path.exists(unix_file_name):
    os.remove(unix_file_name)

while True:
    try:
        result = sock.recv(1024)
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        print(f'Message: {result.decode("utf-8")}')
