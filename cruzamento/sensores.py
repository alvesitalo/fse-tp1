import RPi.GPIO as GPIO

from time import time

class Sensores:
    cruzamento = ''

    sensor_velocidade_1a = 18
    sensor_velocidade_1b = 23

    sensor_velocidade_2a = 24
    sensor_velocidade_2b = 25

    botao_pedestre_1 = [8, 10]
    botao_pedestre_2 = [7, 9]

    def __init__(self, cruzamento):
        self.cruzamento = cruzamento
        self.setup_sensores()

    def setup_sensores(self):
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.sensor_velocidade_1a, GPIO.IN)
        GPIO.setup(self.sensor_velocidade_1b, GPIO.IN)

        GPIO.setup(self.sensor_velocidade_2a, GPIO.IN)
        GPIO.setup(self.sensor_velocidade_2b, GPIO.IN)

        GPIO.setup(self.botao_pedestre_1, GPIO.IN)
        GPIO.setup(self.botao_pedestre_2, GPIO.IN)

    def botoes_pedestre(self, botao):
        print('Apertou o botao 1')
        print(botao)

    def detecta_botoes(self, botao_pedestre_1, botao_pedestre_2, botoes):
        GPIO.add_event_detect(botao_pedestre_1, GPIO.RISING, bouncetime=300)
        GPIO.add_event_detect(botao_pedestre_2, GPIO.RISING, bouncetime=300)

        while 1:
            if GPIO.event_detected(botao_pedestre_1):
                print('botao')
                botoes.append(botao_pedestre_1)
            if GPIO.event_detected(botao_pedestre_2):
                botoes.append(botao_pedestre_2)

    def mede_velocidade(self, sensor_velocidade_a, sensor_velocidade_b, velocidades):
        GPIO.add_event_detect(sensor_velocidade_b, GPIO.RISING)
        GPIO.add_event_detect(sensor_velocidade_a, GPIO.RISING)

        tempo_1 = 0
        tempo_2 = 0
        distancia = 1.0
        velocidade = 0

        while 1:
            if GPIO.event_detected(sensor_velocidade_b):
                tempo_1 = time()
            if GPIO.event_detected(sensor_velocidade_a):
                tempo_2 = time()
                velocidade = distancia / (tempo_2 - tempo_1)
                velocidades.append(velocidade)
                print('Velocidade: ', velocidade)

                if velocidade > 60:
                    print('Excesso de velocidade!')

                tempo_1 = 0
                tempo_2 = 0
                velocidade = 0
