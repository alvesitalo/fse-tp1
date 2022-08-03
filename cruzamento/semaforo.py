import RPi.GPIO as GPIO

class Semaforos:
    cruzamento = ''

    semaforo_1_verde = [1, 2]
    semaforo_1_amarelo = [26, 3]
    semaforo_1_vermelho = [21, 11]

    semaforo_2_verde = [20, 0]
    semaforo_2_amarelo = [16, 5]
    semaforo_2_vermelho = [12, 6]

    def __init__(self, cruzamento):
        self.cruzamento = cruzamento
        self.setup_semaforo()
    
    def setup_semaforo(self):
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.semaforo_1_verde, GPIO.OUT)
        GPIO.setup(self.semaforo_1_amarelo, GPIO.OUT)
        GPIO.setup(self.semaforo_1_vermelho, GPIO.OUT)

        GPIO.setup(self.semaforo_2_verde, GPIO.OUT)
        GPIO.setup(self.semaforo_2_amarelo, GPIO.OUT)
        GPIO.setup(self.semaforo_2_vermelho, GPIO.OUT)

    def estado_inicial(self):
        print('Iniciando Cruzamento s')
        GPIO.output(self.semaforo_1_verde, GPIO.LOW)
        GPIO.output(self.semaforo_1_amarelo, GPIO.LOW)
        GPIO.output(self.semaforo_1_vermelho, GPIO.LOW)

        GPIO.output(self.semaforo_2_verde, GPIO.LOW)
        GPIO.output(self.semaforo_2_amarelo, GPIO.LOW)
        GPIO.output(self.semaforo_2_vermelho, GPIO.LOW)

    def estado_1(self):
        print('Semaforo 1 do Cruzamento s fechado')
        GPIO.output(self.semaforo_1_verde, GPIO.LOW)
        GPIO.output(self.semaforo_1_amarelo, GPIO.LOW)
        GPIO.output(self.semaforo_1_vermelho, GPIO.HIGH)

        print('Semaforo 2 do Cruzamento s aberto')
        GPIO.output(self.semaforo_2_verde, GPIO.HIGH)
        GPIO.output(self.semaforo_2_amarelo, GPIO.LOW)
        GPIO.output(self.semaforo_2_vermelho, GPIO.LOW)

    def estado_2(self):
        GPIO.output(self.semaforo_1_verde, GPIO.LOW)
        GPIO.output(self.semaforo_1_amarelo, GPIO.HIGH)
        GPIO.output(self.semaforo_1_vermelho, GPIO.LOW)

        GPIO.output(self.semaforo_2_verde, GPIO.LOW)
        GPIO.output(self.semaforo_2_amarelo, GPIO.HIGH)
        GPIO.output(self.semaforo_2_vermelho, GPIO.LOW)

    def estado_3(self):
        print('Semaforo 1 do Cruzamento s aberto')
        GPIO.output(self.semaforo_1_verde, GPIO.HIGH)
        GPIO.output(self.semaforo_1_amarelo, GPIO.LOW)
        GPIO.output(self.semaforo_1_vermelho, GPIO.LOW)

        print('Semaforo 2 do Cruzamento s fechado')
        GPIO.output(self.semaforo_2_verde, GPIO.LOW)
        GPIO.output(self.semaforo_2_amarelo, GPIO.LOW)
        GPIO.output(self.semaforo_2_vermelho, GPIO.HIGH)
