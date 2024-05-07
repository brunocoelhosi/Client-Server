import socket
HOST = 'localhost'
PORT = 8002

arquivo = open('1.jpg','rb')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))

sock.send(input('Digite o nome do arquivo:\n').encode())
sock.send(arquivo.read())

confirm = sock.recv(1024)

if confirm == b'ok':
    print('mensagem recebida')