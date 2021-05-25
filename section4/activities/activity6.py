# Crie um modulo para utilizar as funções de cadastro e listagem do exercicio anterior
# O modulo deve ter 4 funções:
#  - Imprimir menu
#  - Ler opção digitada pelo usuário
#  - Ler dados do produto(input) e cadastrar usando o outro modulo
#  - Listar produtos cadastrados do outro modulo

import sys
sys.path.append('.')

from activity4 import cadastrar, listar

def imprimir_menu():
    menu = '''
    Escolha uma das opções:
        1 - Cadastrar
        2 - Listar
        3 - Sair
    '''
    print(menu)

def ler_opcao():
    opcao = int(input('Digite a opção: '))
    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2 :
        imprimir_produtos()
    elif opcao == 3:
        sair()

def cadastrar_produto():
    nome = input('Digite o nome da bebidas: ')
    descricao = input('Digite a descricao da bebidas: ')
    tipo = input('Digite o tipo da bebidas: ')
    preco = input('Digite o preco da bebidas: ')
    msg = cadastrar(nome, descricao, tipo, preco)
    print(msg)

def imprimir_produtos():
    for e in listar():
        print(e)

def sair():
    print('Saindo ...')

continuar = True

while continuar:
    imprimir_menu()
    ler_opcao()
    resposta = input('Deseja continuar? (s/n)')
    if resposta != 's':
        continuar = False
