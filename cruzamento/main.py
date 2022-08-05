
from servidor import Servidor
from cruzamento import Cruzamento

def main():
    print('----------------------------------------------------')
    print('|       Bem-vindo ao Sistema de Cruzamentos!       |')
    print('----------------------------------------------------\n')

    print('Para comecar, digite a opcao de servidor que deseja utilizar:')
    print('0 - Servidor Central')
    print('1 - Cruzamento 3')
    print('2 - Cruzamento 4')
    print('3 - Sair\n')

    servidor_central = ('164.41.98.26', 10210)
    servidor_c1 = ('164.41.98.17', 10201)
    servidor_c2 = ('164.41.98.17', 10202)
    servidor_c3 = ('164.41.98.26', 10203)
    servidor_c4 = ('164.41.98.26', 10204)
    
    opcao = -1

    while opcao != 3:
        opcao = int(input('Opcao: '))

        if opcao == 0:
            print('Voce escolheu o Servidor Central!\n')
            #Cruzamento('1', *servidor_c1)
            #Cruzamento('2', *servidor_c2)
            Servidor(servidor_central, servidor_c1, servidor_c2, servidor_c3, servidor_c4)
        elif opcao == 1:
            print('Voce escolheu o Cruzamento 3!\n')
            Cruzamento('3', *servidor_c3)
        elif opcao == 2:
            print('Voce escolheu o Cruzamento 4!\n')
            Cruzamento('4', *servidor_c4)
        elif opcao == 3:
            print('Saindo...\n')
        else:
            print('Opcao invalida')

main()
