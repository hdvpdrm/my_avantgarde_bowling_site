import socket
import sys


class Server:
    def __init__(self, port: int):
        self.port = port
        self.host = "127.0.0.1"
        
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        print("fuck em all")
        self.server_socket.listen(5)
        
        print(f"Server listening on {self.host}:{self.port}")


    def run(self) -> None:
        client_socket, addr = self.server_socket.accept()
        print(f"Got a connection from {addr}")

        try:
            while True:
                data = client_socket.recv(1024)
                #if not data:
                #    break
                if data:
                    print(f"Received: {data.decode()}") 
        except Exception as e:
            print(str(e))
        finally:
            client_socket.close()
