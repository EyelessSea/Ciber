import socket
import threading

def handle_client(conn, address):
    print(f"Conexión establecida con: {address}")
    data = conn.recv(1024)
    print(f"Recibir mensaje del cliente: {data.decode()}")
    conn.send("Hola a todos".encode())
    conn.close()

def start_server():
    s = socket.socket()
    s.bind(('127.0.0.1', 8000))
    s.listen()

    print('El servidor está comenzando ...')

    while True:
        conn, address = s.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, address))
        client_thread.start()

if __name__ == "__main__":
    start_server()
