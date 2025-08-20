import socket
import threading

ip = "10.34.77.0"
port = 12345
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
running = True


def main():
    server.bind(("0.0.0.0", port))
    threading.Thread(target=wait_server).start()
    a = input("Target IP: ")
    server.connect((a, port))
    server.send(bytes("Hello from the client!", "utf-8"))
    print(str(server.recv(1024), "utf-8"))



    
def wait_server():
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
    except Exception as e:
        print(f"An error occurred: {e}")
        running = False
        server.close()