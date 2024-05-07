import socket
HOST = 'localhost'
PORT = 8002

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((HOST, PORT))

#n° de clients
sock.listen(5)
#
##enviando mensagem
#while True:
#    novoSock, _ = sock.accept()
#    mensagem = novoSock.recv(1024).decode()
#    novoSock.send(b'ok')
#    print(mensagem)

while True:
    novoSock, _ = sock.accept()
    nomeArquivo = novoSock.recv(1024).decode()
    novoArquivo = novoSock.recv(1000000000)

    with open(f'arquivos/{nomeArquivo}','wb') as arq:
        arq.write(novoArquivo)

    novoSock.send(b'ok')