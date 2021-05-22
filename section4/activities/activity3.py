# Crie um sistema de cadastro de prudutos seguindo os seguintes requisitos:
# 1 - O usuário poderá cadastrar quantos produtos quiser
# 2 - O sistema deverá ter um menu para cadastrar, listar e deletar produtos
# 3 - O produto deve ter nome, descrição e valor
# 4 - Deve ser criado uma função para cada operação a seguir:
#  -- imprimir menu
#  -- cadastrar produto
#  -- listar produto
#  -- excluir produto
lista_produtos = []

def menu():
    menu = '''
        1 - Cadastrar
        2 - Listar
        3 - Deletar
    '''

    print(menu)
    opcao = int(input('Digite uma opção: '))
    return opcao

def escolhe_operacao(opt):
    if opt == 1:
        cadastrar()
    elif opt == 2:
        listar()
    elif opt == 3:
        deletar()

def cadastrar():
    nome = input('Digite o nome do produto: ')
    descricao = input('Digite a descricao do produto: ')
    valor = input('Digite o valor do produto: ')
    produto = {'nome': nome, 'descricao': descricao, 'valor': valor}
    lista_produtos.append(produto)

def listar():
    for p in lista_produtos:
        print(f''''
            nome: {p['nome']} - descricao: {p['descricao']} - valor: {p['valor']}
        ''')

def deletar():
    listar()
    prod_del = input('Digite o nome do produto que deseja deletar: ')
    
    for p in lista_produtos:
        if p['nome'] == prod_del:
            lista_produtos.remove(p)

opt = menu()
escolhe_operacao(opt)

 