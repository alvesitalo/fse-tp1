# FSE - Trabalho 1
Trabalho 1 da Disciplina de Fundamentos de Sistemas Embarcados.

## Instalação

1. Clonar o repositório nas duas placas;
2. Entrar na pasta *cruzamento* do projeto.

## Execução

Pela Raspberry 43 (164.41.98.17):

1. Iniciar o Cruzamento 1:
    ```
    python main.py
    1
    ```
2. Iniciar o Cruzamento 2:
    ```
    python main.py
    2
    ```

Pela Raspberry 44 (164.41.98.26):

3. Iniciar o Cruzamento 3:
    ```
    python main.py
    3
    ```  
4. Iniciar o Cruzamento 4:
    ```
    python main.py
    4
    ```  
5. Iniciar o Servidor Central:
    ```
    python main.py
    0
    ```  

6. Escolher o modo de execução: (Normal, Noturno ou Emergência):
    ```
    1
    2
    3
    ```

**Importante**: O servidor central somente deve ser iniciado **após todos os cruzamentos** estarem funcionando.

## Mudança de IP e Porta

As mudanças podem ser realizadas no arquivo *main.py* nas variáveis de servidor.
