import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(('127.0.0.1', 8888))
    sock.listen(5)
    sock.settimeout(5)
    # sock.settimeout(0) -> sock.setblocking(False)
    # sock.settimeout(None) -> sock.setblocking(True)

    while True:
        try:
            client, addr = sock.accept()
        except socket.error:
            print('No clients')
        except KeyboardInterrupt:
            break
        else:
            result = client.recv(1024)
            client.close()
            print(f'Message: {result.decode("utf-8")}')
