
from servidor import Servidor
from cruzamento import Cruzamento

def main():
    print('----------------------------------------------------')
    print('|       Bem-vindo ao Sistema de Cruzamentos!       |')
    print('----------------------------------------------------\n')

    print('Para comecar, digite a opcao que deseja conectar:')
    print('0 - Servidor Central')
    print('1 - Cruzamento 1')
    print('2 - Cruzamento 2')
    print('3 - Cruzamento 3')
    print('4 - Cruzamento 4')
    print('5 - Sair\n')

    servidor_central = ('164.41.98.26', 10210)
    servidor_c1 = ('164.41.98.17', 10201)
    servidor_c2 = ('164.41.98.17', 10202)
    servidor_c3 = ('164.41.98.26', 10203)
    servidor_c4 = ('164.41.98.26', 10204)
    
    opcao = -1

    while opcao != 5:
        opcao = int(input('Opcao: '))

        if opcao == 0:
            print('Voce escolheu o Servidor Central!\n')
            Servidor(servidor_central, servidor_c1, servidor_c2, servidor_c3, servidor_c4)
        elif opcao == 1:
            print('Voce escolheu o Cruzamento 1!\n')
            Cruzamento('1', *servidor_c1)
        elif opcao == 2:
            print('Voce escolheu o Cruzamento 2!\n')
            Cruzamento('2', *servidor_c2)
        elif opcao == 3:
            print('Voce escolheu o Cruzamento 3!\n')
            Cruzamento('3', *servidor_c3)
        elif opcao == 4:
            print('Voce escolheu o Cruzamento 4!\n')
            Cruzamento('4', *servidor_c4)
        elif opcao == 5:
            print('Saindo...\n')
        else:
            print('Opcao invalida')

main()
