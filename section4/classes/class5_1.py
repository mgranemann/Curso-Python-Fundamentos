#Modulos

# criação de modulo para cadastro e listagem de produtos

# variável global para armazenar a lista de produtos
lista_produtos = []

# função de cadastro de produtos
# recebe 3 parâmetros , cria um dicionário e adiciona a lista global
# retorna uma mensagem do tipo string
def cadastrar(nome, descricao, preco):
    produto = {'nome': nome, 'descricao': descricao, 'preco':preco}
    lista_produtos.append(produto)
    return 'Cadastrado com sucesso!'

# função para retornar a lista de produtos
# função nao recebe nenhum parâmetro
# função retorna uma variável global com a lista de produtos
def listar():
    return lista_produtos