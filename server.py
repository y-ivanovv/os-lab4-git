import http.server
import socketserver

PORT = 8080

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as server:
        print(f"Сервер запущен на порту {PORT}", flush=True)
        server.serve_forever()
