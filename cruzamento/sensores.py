import RPi.GPIO as GPIO

from time import time

class Sensores:
    cruzamento = ''

    sensor_vel_1a = 18
    sensor_vel_1b = 23

    sensor_vel_2a = 24
    sensor_vel_2b = 25

    botao_ped_1 = [8, 10]
    botao_ped_2 = [7, 9]

    def __init__(self, cruzamento):
        self.cruzamento = cruzamento
        self.setup_sensores()

    def setup_sensores(self):
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.sensor_vel_1a, GPIO.IN)
        GPIO.setup(self.sensor_vel_1b, GPIO.IN)

        GPIO.setup(self.sensor_vel_2a, GPIO.IN)
        GPIO.setup(self.sensor_vel_2b, GPIO.IN)

        GPIO.setup(self.botao_ped_1, GPIO.IN)
        GPIO.setup(self.botao_ped_2, GPIO.IN)

    def detecta_pedestre(self, botao_ped_1, botao_ped_2, botoes):
        GPIO.add_event_detect(botao_ped_1, GPIO.RISING, bouncetime=300)
        GPIO.add_event_detect(botao_ped_2, GPIO.RISING, bouncetime=300)

        while 1:
            if GPIO.event_detected(botao_ped_1):
                botoes.append(botao_ped_1)
            if GPIO.event_detected(botao_ped_2):
                botoes.append(botao_ped_2)

    def mede_velocidade(self, sensor_vel_a, sensor_vel_b, velocidades):
        GPIO.add_event_detect(sensor_vel_b, GPIO.RISING)
        GPIO.add_event_detect(sensor_vel_a, GPIO.RISING)

        tempo_1 = 0
        tempo_2 = 0
        distancia = 0.001 # 1m em km
        velocidade = 0

        while 1:
            if GPIO.event_detected(sensor_vel_b):
                tempo_1 = time()
            if GPIO.event_detected(sensor_vel_a):
                tempo_2 = time()
                velocidade = distancia / ((tempo_2 - tempo_1) / 3600)
                velocidades.append(velocidade)
                print('Velocidade: ', velocidade)

                if velocidade > 60:
                    print('Excesso de velocidade!')

                tempo_1 = 0
                tempo_2 = 0
                velocidade = 0
