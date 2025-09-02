import socket
import threading

ip = "10.34.77.0"
listen_port = 12345
send_port = 54321
send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
running = True


def main():
    threading.Thread(target=wait_server).start()
    a = input("Target IP: ")
    send_socket.connect((a, listen_port))
    send_socket.send(bytes("Hello from the client!", "utf-8"))



    
def wait_server():
    server.bind(("0.0.0.0", listen_port))
    while running:
        server.listen(5)
        conn, addr = server.accept()
        print(f"Connection from {addr} has been established.")
        conn.send(bytes("Welcome to the server!", "utf-8"))
        response = server.recv(1024)
        print(str(response, "utf-8"))



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Server is shutting down.")
        running = False
        server.close()
        send_socket.close()
    except Exception as e:
        print(f"An error occurred: {e}")
        running = False
        server.close()
        send_socket.close()