import socket
import json

from threading import Thread
from time import sleep, time

class Servidor:
    servidor_central = ('', 0)
    servidor_c1 = ('', 0)
    servidor_c2 = ('', 0)
    servidor_c3 = ('', 0)
    servidor_c4 = ('', 0)

    tcp_c1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_c2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_c3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_c4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    vel_log_c1 = []
    vel_log_c2 = []
    vel_log_c3 = []
    vel_log_c4 = []

    vel_media_c1 = 0
    vel_media_c2 = 0
    vel_media_c3 = 0
    vel_media_c4 = 0

    botao_ped_1 = False
    botao_ped_2 = False

    def __init__(self, servidor_central, servidor_c1, servidor_c2, servidor_c3, servidor_c4):
        self.servidor_c1 = servidor_c1
        self.servidor_c2 = servidor_c2
        self.servidor_c3 = servidor_c3
        self.servidor_c4 = servidor_c4
        self.conecta_sockets()

    def rotina_semafaro(self):
        while 1:
            dados_estado_3 = {
                "tipo": "acao",
                "estado": 3,
            }
            self.tcp_c1.sendall(bytes(json.dumps(dados_estado_3), encoding='utf-8'))
            self.tcp_c2.sendall(bytes(json.dumps(dados_estado_3), encoding='utf-8'))
            self.tcp_c3.sendall(bytes(json.dumps(dados_estado_3), encoding='utf-8'))
            self.tcp_c4.sendall(bytes(json.dumps(dados_estado_3), encoding='utf-8'))
            sleep(5)
            if not self.botao_ped_1:
                sleep(5)
            self.botao_ped_1 = False

            dados_estado_2 = {
                "tipo": "acao",
                "estado": 2,
            }
            self.tcp_c1.sendall(bytes(json.dumps(dados_estado_2), encoding='utf-8'))
            self.tcp_c2.sendall(bytes(json.dumps(dados_estado_2), encoding='utf-8'))
            self.tcp_c3.sendall(bytes(json.dumps(dados_estado_2), encoding='utf-8'))
            self.tcp_c4.sendall(bytes(json.dumps(dados_estado_2), encoding='utf-8'))
            sleep(3)

            dados_estado_1 = {
                "tipo": "acao",
                "estado": 1,
            }
            self.tcp_c1.sendall(bytes(json.dumps(dados_estado_1), encoding='utf-8'))
            self.tcp_c2.sendall(bytes(json.dumps(dados_estado_1), encoding='utf-8'))
            self.tcp_c3.sendall(bytes(json.dumps(dados_estado_1), encoding='utf-8'))
            self.tcp_c4.sendall(bytes(json.dumps(dados_estado_1), encoding='utf-8'))
            sleep(10)
            if not self.botao_ped_2:
                sleep(10)
            self.botao_ped_2 = False

            dados_estado_4 = {
                "tipo": "acao",
                "estado": 4,
            }
            self.tcp_c1.sendall(bytes(json.dumps(dados_estado_4), encoding='utf-8'))
            self.tcp_c2.sendall(bytes(json.dumps(dados_estado_4), encoding='utf-8'))
            self.tcp_c3.sendall(bytes(json.dumps(dados_estado_4), encoding='utf-8'))
            self.tcp_c4.sendall(bytes(json.dumps(dados_estado_4), encoding='utf-8'))
            sleep(3)             

    def modo_noturno(self):
        dados_estado_5 = {
            "tipo": "acao",
            "estado": 5,
        }
        self.tcp_c1.sendall(bytes(json.dumps(dados_estado_5), encoding='utf-8'))
        self.tcp_c2.sendall(bytes(json.dumps(dados_estado_5), encoding='utf-8'))
        self.tcp_c3.sendall(bytes(json.dumps(dados_estado_5), encoding='utf-8'))
        self.tcp_c4.sendall(bytes(json.dumps(dados_estado_5), encoding='utf-8'))
    
    def recebe_dados(self, dados):
        #print(dados)
        dados = json.loads(dados)

        if dados['tipo'] == 'velocidade_1' or dados['tipo'] == 'velocidade_2':
            if dados['cruzamento'] == '1':
                self.vel_log_c1 = self.vel_log_c1 + dados['estado']
            if dados['cruzamento'] == '2':
                self.vel_log_c2 = self.vel_log_c2 + dados['estado']
            if dados['cruzamento'] == '3':
                self.vel_log_c3 = self.vel_log_c3 + dados['estado']
            if dados['cruzamento'] == '4':
                self.vel_log_c4 = self.vel_log_c4 + dados['estado']
        if dados['tipo'] == 'ped_1' and dados['estado']:
            self.botao_ped_1 = True
        if dados['tipo'] == 'ped_2' and dados['estado']:
            self.botao_ped_2 = True
    
    def conecta_cruzamento_1(self):
        self.tcp_c1.connect(self.servidor_c1)
        print('Conectado ao Cruzamento 1\n')
        while 1:
            data = self.tcp_c1.recv(1024)
            if data:
                self.recebe_dados(data.decode())

    def conecta_cruzamento_2(self):
        self.tcp_c2.connect(self.servidor_c2)
        print('Conectado ao Cruzamento 2\n')
        while 1:
            data = self.tcp_c2.recv(1024)
            if data:
                self.recebe_dados(data.decode())

    def conecta_cruzamento_3(self):
        self.tcp_c3.connect(self.servidor_c3)
        print('Conectado ao Cruzamento 3\n')
        while 1:
            data = self.tcp_c3.recv(1024)
            if data:
                self.recebe_dados(data.decode())

    def conecta_cruzamento_4(self):
        self.tcp_c4.connect(self.servidor_c4)
        print('Conectado ao Cruzamento 4\n')
        while 1:
            data = self.tcp_c4.recv(1024)
            if data:
                self.recebe_dados(data.decode())

    def conecta_sockets(self):
        thread_c1 = Thread(target=self.conecta_cruzamento_1, args=())
        thread_c1.start()

        thread_c2 = Thread(target=self.conecta_cruzamento_2, args=())
        thread_c2.start()

        thread_c3 = Thread(target=self.conecta_cruzamento_3, args=())
        thread_c3.start()

        thread_c4 = Thread(target=self.conecta_cruzamento_4, args=())
        thread_c4.start()

        thread_semaforo = Thread(target=self.rotina_semafaro, args=())
        thread_semaforo.start()

        thread_noturno = Thread(target=self.modo_noturno, args=())

        while 1:
            op = input()
            if op == '1':
                thread_semaforo.join(1)
                thread_noturno.start()
            else:
                thread_semaforo.start()
                thread_noturno.join(1)

        thread_c1.join()
        thread_c2.join()
        thread_c3.join()
        thread_c4.join()
        thread_semaforo.join()
        sys.exit()
