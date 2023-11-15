import socket

class Client:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        try:
            self.s.connect(('127.0.0.1', 8000))
            self.s.send(b'Hola desde el Cliente!')
            data = self.s.recv(1024)
            print(f"Recibir mensaje del servidor: {data.decode()}")
        except Exception as e:
            print(f"Error en la conexión: {e}")
        finally:
            self.s.close()

if __name__ == "__main__":
    client = Client()
    client.run()
