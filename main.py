import socket
import threading


class DirtServerClient:
    def __init__(self, listen_port=12345):
        self.listen_port = listen_port
        self.send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.running = True
        self.server_thread = threading.Thread(target=self.wait_server)
        self.server_thread.daemon = True

    def start(self):
        self.server_thread.start()
        target_ip = input("Target IP: ")
        self.send_socket.connect((target_ip, self.listen_port))
        self.send_socket.send(bytes("Hello from the client!", "utf-8"))

    def wait_server(self):
        self.server.bind(("0.0.0.0", self.listen_port))
        self.server.settimeout(1)
        while self.running:
            try:
                self.server.listen(5)
                conn, addr = self.server.accept()
                print(f"Connection from {addr} has been established.")
                conn.send(bytes("Welcome to the server!", "utf-8"))
                response = conn.recv(1024)
                print(str(response, "utf-8"))
                conn.close()
            except socket.timeout:
                continue
            except Exception as e:
                print(f"Server error: {e}")
                break

    def close(self):
        self.running = False
        try:
            self.server.close()
        except Exception:
            pass
        try:
            self.send_socket.close()
        except Exception:
            pass
        print("Server is shutting down.")

    def __del__(self):
        self.close()


if __name__ == "__main__":
    dirt = DirtServerClient()
    try:
        dirt.start()
    except KeyboardInterrupt:
        dirt.close()
    except Exception as e:
        print(f"An error occurred: {e}")
        dirt.close()