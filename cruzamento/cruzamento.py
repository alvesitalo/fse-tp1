import socket
import json

from threading import Thread
from time import sleep

from semaforos import Semaforos
from sensores import Sensores

class Cruzamento:
    nome = ''
    host = ''
    port = 0
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    sem = Semaforos(nome)
    sen = Sensores(nome)

    ped_1 = []
    ped_2 = []
    velocidades_1 = []
    velocidades_2 = []

    def __init__(self, nome, host, port):
        self.nome = nome
        self.host = host
        self.port = port
        self.inicia_cruzamento()

    def envia_dados(self, connection):
        while 1:
            sleep(0.9)
            dados_ped_1 = {
                'tipo': 'ped_1',
                'cruzamento': self.nome,
                'estado': self.ped_1,
            }
            connection.sendall(bytes(json.dumps(dados_ped_1), encoding='utf-8'))
            self.ped_1.clear()

            sleep(0.1)
            dados_ped_2 = {
                'tipo': 'ped_2',
                'cruzamento': self.nome,
                'estado': self.ped_2,
            }
            connection.sendall(bytes(json.dumps(dados_ped_2), encoding='utf-8'))
            self.ped_2.clear()

            sleep(0.9)
            dados_velocidade_1 = {
                'tipo': 'velocidade_1',
                'cruzamento': self.nome,
                'estado': self.velocidades_1,
            }
            connection.sendall(bytes(json.dumps(dados_velocidade_1), encoding='utf-8'))
            self.velocidades_1.clear()
            
            sleep(0.1)
            dados_velocidade_2 = {
                'tipo': 'velocidade_2',
                'cruzamento': self.nome,
                'estado': self.velocidades_2,
            }
            connection.sendall(bytes(json.dumps(dados_velocidade_2), encoding='utf-8'))
            self.velocidades_2.clear()

    def recebe_dados(self, dados):
        #print(dados)
        dados = json.loads(dados)

        if dados['tipo'] == 'acao':
            if dados['estado'] == 0:
                self.sem.estado_inicial()
            elif dados['estado'] == 1:
                self.sem.estado_1()
            elif dados['estado'] == 2:
                self.sem.estado_2()
            elif dados['estado'] == 3:
                self.sem.estado_3()
            elif dados['estado'] == 4:
                self.sem.estado_4()
            elif dados['estado'] == 5:
                self.sem.estado_noturno()
            elif dados['estado'] == 6:
                self.sem.estado_emergencia()
    
    def inicia_cruzamento(self):
        self.tcp.bind(('0.0.0.0', self.port))
        self.tcp.listen()
        print('Servidor do Cruzamento iniciado (:%s)' %self.port)

        conn, addr = self.tcp.accept()
        print('Conectado com o Servidor Central\n')

        thread_velocidade_1 = Thread(target=self.sen.mede_velocidade, args=(self.sen.sensor_vel_1a, self.sen.sensor_vel_1b, self.velocidades_1))
        thread_velocidade_1.start()
        
        thread_velocidade_2 = Thread(target=self.sen.mede_velocidade, args=(self.sen.sensor_vel_2a, self.sen.sensor_vel_2b, self.velocidades_2))
        thread_velocidade_2.start()

        thread_ped_1 = Thread(target=self.sen.detecta_pedestre, args=(self.sen.botao_ped_1[0], self.sen.botao_ped_1[1], self.ped_1))
        thread_ped_1.start()

        thread_ped_2 = Thread(target=self.sen.detecta_pedestre, args=(self.sen.botao_ped_2[0], self.sen.botao_ped_2[1], self.ped_2))
        thread_ped_2.start()

        thread_dados = Thread(target=self.envia_dados, args=(conn,))
        thread_dados.start()

        while 1:
            data = conn.recv(1024)
            if data:
                self.recebe_dados(data.decode())

        thread_velocidade_1.join()
        thread_velocidade_2.join()
        thread_ped_1.join()
        thread_ped_2.join()
        thread_dados.join()
        sys.exit()
