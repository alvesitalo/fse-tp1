import socket
import json

from semaforo import estado_inicial, estado_1, estado_2, estado_3

tcp_servidor_central
tcp_servidor_distribuido1
tcp_servidor_distribuido2

def rotina_semafaro():
    while 1:
        dados_estado_3 = {
            "tipo": "acao",
            "estado": 3
        }
        tcp_servidor_distribuido1.sendall(bytes(json.dumps(dados_estado_3), encoding='utf-8'))
        tcp_servidor_distribuido2.sendall(bytes(json.dumps(dados_estado_3), encoding='utf-8'))
        sleep(5)

        dados_estado_2 = {
            "tipo": "acao",
            "estado": 2
        }
        tcp_servidor_distribuido1.sendall(bytes(json.dumps(dados_estado_2), encoding='utf-8'))
        tcp_servidor_distribuido2.sendall(bytes(json.dumps(dados_estado_2), encoding='utf-8'))
        sleep(3)

        dados_estado_1 = {
            "tipo": "acao",
            "estado": 1
        }
        tcp_servidor_distribuido1.sendall(bytes(json.dumps(dados_estado_1), encoding='utf-8'))
        tcp_servidor_distribuido2.sendall(bytes(json.dumps(dados_estado_1), encoding='utf-8'))
        sleep(5)

        dados_estado_2 = {
            "tipo": "acao",
            "estado": 2
        }
        tcp_servidor_distribuido1.sendall(bytes(json.dumps(dados_estado_2), encoding='utf-8'))
        tcp_servidor_distribuido2.sendall(bytes(json.dumps(dados_estado_2), encoding='utf-8'))
        sleep(3)

def conecta_servidor_distribuido_1(host, port):
    tcp_servidor_distribuido1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_servidor_distribuido1.connect((host, port))
    print('Conectado ao Servidor Distribuido 1')

def conecta_servidor_distribuido_2(host, port):
    tcp_servidor_distribuido2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_servidor_distribuido2.connect((host, port))
    print('Conectado ao Servidor Distribuido 2')

def recebe_dados(dados):
    dados = json.loads(dados)
    print(dados)

def inicia_servidor_central(servidor_c1, servidor_d1, servidor_d2):
    """Servidor central do sistema de cruzamentos."""

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.bind((host, port))
    tcp.listen()
    print('Servidor central iniciado\n')

    conn, addr = tcp.accept()
    print('Conectado com: ', addr)

    conecta_servidor_distribuido_1(servidor_d1)
    conecta_servidor_distribuido_2(servidor_d2)
    
    rotina_semafaro()

    while 1:
        data = conn.recv(1024)
        if data:
            recebe_dados(data.decode())
            conn.sendall(bytes('success', encoding='utf-8'))
