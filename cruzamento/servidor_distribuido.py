import socket
import json

from semaforo import estado_inicial, estado_1, estado_2, estado_3

def recebe_dados(dados):
    dados = json.loads(dados)

    if dados['tipo'] == 'acao':
        if dados['estado'] == 0:
            estado_inicial()
        elif dados['estado'] == 1:
            estado_1()
        elif dados['estado'] == 2:
            estado_2()
        elif dados['estado'] == 3:
            estado_3()
    print(dados)

def inicia_servidor_distribuido(host, port):
    """Servidor distribuido do sistema de cruzamentos."""

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.bind((host, port))
    tcp.listen()
    print('Servidor distribuido iniciado\n')

    conn, addr = s.accept()
    print('Conectado com o Servidor Central')

    while 1:
        data = conn.recv(1024)
        if data:
            recebe_dados(data.decode())
            conn.sendall(bytes('success', encoding='utf-8'))
