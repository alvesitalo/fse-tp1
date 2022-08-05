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

        self.estado_inicial()

    def estado_inicial(self):
        GPIO.output(self.semaforo_1_verde, GPIO.LOW)
        GPIO.output(self.semaforo_1_amarelo, GPIO.LOW)
        GPIO.output(self.semaforo_1_vermelho, GPIO.LOW)

        GPIO.output(self.semaforo_2_verde, GPIO.LOW)
        GPIO.output(self.semaforo_2_amarelo, GPIO.LOW)
        GPIO.output(self.semaforo_2_vermelho, GPIO.LOW)

    def estado_1(self):
        GPIO.output(self.semaforo_1_verde, GPIO.LOW)
        GPIO.output(self.semaforo_1_amarelo, GPIO.LOW)
        GPIO.output(self.semaforo_1_vermelho, GPIO.HIGH)

        GPIO.output(self.semaforo_2_verde, GPIO.HIGH)
        GPIO.output(self.semaforo_2_amarelo, GPIO.LOW)
        GPIO.output(self.semaforo_2_vermelho, GPIO.LOW)

    def estado_2(self):
        GPIO.output(self.semaforo_1_verde, GPIO.LOW)
        GPIO.output(self.semaforo_1_amarelo, GPIO.HIGH)
        GPIO.output(self.semaforo_1_vermelho, GPIO.LOW)

        GPIO.output(self.semaforo_2_verde, GPIO.LOW)
        GPIO.output(self.semaforo_2_amarelo, GPIO.LOW)
        GPIO.output(self.semaforo_2_vermelho, GPIO.HIGH)

    def estado_3(self):
        GPIO.output(self.semaforo_1_verde, GPIO.HIGH)
        GPIO.output(self.semaforo_1_amarelo, GPIO.LOW)
        GPIO.output(self.semaforo_1_vermelho, GPIO.LOW)

        GPIO.output(self.semaforo_2_verde, GPIO.LOW)
        GPIO.output(self.semaforo_2_amarelo, GPIO.LOW)
        GPIO.output(self.semaforo_2_vermelho, GPIO.HIGH)

    def estado_4(self):
        GPIO.output(self.semaforo_1_verde, GPIO.LOW)
        GPIO.output(self.semaforo_1_amarelo, GPIO.LOW)
        GPIO.output(self.semaforo_1_vermelho, GPIO.HIGH)

        GPIO.output(self.semaforo_2_verde, GPIO.LOW)
        GPIO.output(self.semaforo_2_amarelo, GPIO.HIGH)
        GPIO.output(self.semaforo_2_vermelho, GPIO.LOW)

    def estado_noturno(self):
        self.estado_inicial()

        GPIO.PWM(self.semaforo_1_amarelo[0], 0.5).start(10)
        GPIO.PWM(self.semaforo_1_amarelo[1], 0.5).start(10)
        GPIO.PWM(self.semaforo_2_amarelo[0], 0.5).start(10)
        GPIO.PWM(self.semaforo_2_amarelo[1], 0.5).start(10)
