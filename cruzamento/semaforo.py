import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

semaforo_1_verde = [1, 2]
semaforo_1_amarelo = [26, 3]
semaforo_1_vermelho = [21, 11]

semaforo_2_verde = [20, 0]
semaforo_2_amarelo = [16, 5]
semaforo_2_vermelho = [12, 6]

GPIO.setup(semaforo_1_verde, GPIO.OUT)
GPIO.setup(semaforo_1_amarelo, GPIO.OUT)
GPIO.setup(semaforo_1_vermelho, GPIO.OUT)

GPIO.setup(semaforo_2_verde, GPIO.OUT)
GPIO.setup(semaforo_2_amarelo, GPIO.OUT)
GPIO.setup(semaforo_2_vermelho, GPIO.OUT)

def estado_inicial():
    print('Iniciando Cruzamento s')
    GPIO.output(semaforo_1_verde, GPIO.LOW)
    GPIO.output(semaforo_1_amarelo, GPIO.LOW)
    GPIO.output(semaforo_1_vermelho, GPIO.LOW)

    GPIO.output(semaforo_2_verde, GPIO.LOW)
    GPIO.output(semaforo_2_amarelo, GPIO.LOW)
    GPIO.output(semaforo_2_vermelho, GPIO.LOW)

def estado_1():
    print('Semaforo 1 do Cruzamento s fechado')
    GPIO.output(semaforo_1_verde, GPIO.LOW)
    GPIO.output(semaforo_1_amarelo, GPIO.LOW)
    GPIO.output(semaforo_1_vermelho, GPIO.HIGH)

    print('Semaforo 2 do Cruzamento s aberto')
    GPIO.output(semaforo_2_verde, GPIO.HIGH)
    GPIO.output(semaforo_2_amarelo, GPIO.LOW)
    GPIO.output(semaforo_2_vermelho, GPIO.LOW)

def estado_2():
    GPIO.output(semaforo_1_verde, GPIO.LOW)
    GPIO.output(semaforo_1_amarelo, GPIO.HIGH)
    GPIO.output(semaforo_1_vermelho, GPIO.LOW)

    GPIO.output(semaforo_2_verde, GPIO.LOW)
    GPIO.output(semaforo_2_amarelo, GPIO.HIGH)
    GPIO.output(semaforo_2_vermelho, GPIO.LOW)

def estado_3():
    print('Semaforo 1 do Cruzamento s aberto')
    GPIO.output(semaforo_1_verde, GPIO.HIGH)
    GPIO.output(semaforo_1_amarelo, GPIO.LOW)
    GPIO.output(semaforo_1_vermelho, GPIO.LOW)

    print('Semaforo 2 do Cruzamento s fechado')
    GPIO.output(semaforo_2_verde, GPIO.LOW)
    GPIO.output(semaforo_2_amarelo, GPIO.LOW)
    GPIO.output(semaforo_2_vermelho, GPIO.HIGH)
