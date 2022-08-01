
from servidor_central import inicia_servidor_central
from servidor_distribuido import inicia_servidor_distribuido

def main():
    print('----------------------------------------------------')
    print('|       Bem-vindo ao Sistema de Cruzamentos!       |')
    print('----------------------------------------------------\n')

    print('Para comecar, digite a opcao de servidor que deseja utilizar:')
    print('1 - Servidor Central')
    print('2 - Servidor Distribuido 1')
    print('3 - Servidor Distribuido 2')
    print('0 - Sair\n')

    servidor_c1 = ('0.0.0.0', 10210)
    servidor_d1 = ('164.41.98.17', 10201)
    servidor_d2 = ('164.41.98.26', 10202)
    
    opcao = -1

    while opcao != 0:
        opcao = int(input('Opcao: '))

        if opcao == 1:
            print('Voce escolheu o Servidor Central!\n')
            inicia_servidor_central(servidor_c1, servidor_d1, servidor_d2)
        elif opcao == 2:
            print('Voce escolheu o Servidor Distribuido 1!\n')
            inicia_servidor_distribuido(servidor_d1)
        elif opcao == 3:
            print('Voce escolheu o Servidor Distribuido 2!\n')
            inicia_servidor_distribuido(servidor_d2)
        elif opcao == 0:
            print('Saindo...\n')
        else:
            print('Opcao invalida')
