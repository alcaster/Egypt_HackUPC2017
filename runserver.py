import sys

from app import app

DEFAULT_HOST = "localhost"
DEFAULT_PORT = "8000"

if __name__ == '__main__':
    try:
        host, port = sys.argv[1:3]
        app.run(host, port)
    except (IndexError, ValueError):
        print("Wrong arguments. Expected <host> <port>. Running on default.")
        app.run(DEFAULT_HOST, DEFAULT_PORT)
