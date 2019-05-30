import socket
import subprocess
import sys

# configurazione del server
url = ""  # indirizzo IP a cui bindare il server
port = 15000  # porta sulla quale risponde il server


def ricevi_comandi(url, port, conn, sock):
    try:
        while True:
            richiesta = conn.recv(4096)
            # print(richiesta)  # debug richiesta server
            if richiesta == b"":
                print("Sto riavviando il server")
                sock.close()
                sub_server(url, port, backlog=1)
            elif richiesta == b"kill-server":
                print("Sto killando il server")
                sys.exit(0)
            else:
                risposta = subprocess.run(
                    richiesta.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                data = risposta.stdout + risposta.stderr
                conn.sendall(data)
    except ConnectionResetError:
        print("La connessione al Client é stata interrotta. Riavvio il Server")
        sock.close()
        sub_server(url, port, backlog=1)
        # sys.exit(0)


def sub_server(url, port, backlog=1):
    try:
        sock = socket.socket()
        sock.bind((url, port))
        # print(url) # debug indirizzo server
        # print(port) # debug porta server
        sock.listen(backlog)
        print(f"Server Inizializzato. In ascolto...")
    except socket.error as errore:
        print(f"Qualcosa è andato storto... \n{errore}")
        print(f"Sto tentando di reinizializzare il server...")
        sock.close()
        sub_server(url, port, backlog=1)
    conn, indirizzo_client = sock.accept()  # conn = socket_client
    print(f"Connessione Server - Client Stabilita: {indirizzo_client}")
    ricevi_comandi(url, port, conn, sock)


if __name__ == '__main__':
    sub_server(url, port)
