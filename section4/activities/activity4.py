# Crie uma função para cadastro de bebidas.
# A função deve conter os seguites parâmetros:
# - nome
# - descrição
# - tipo
# - preco
# A função deve salvar os produtos em uma lista global que poderá armazenar no maximo 10 itens
# Caso o limite seja ultrapassado, a função deve retornar uma mensagem de erro do tipo string
# Caso o limite não tenha sido ultrapassado, a função deve retornar uma mensagem de sucesso do tipo string
# A função deve ser criada em um modulo separado do módulo onde será executada 



lista = []

def cadastrar(nome, descricao, tipo, preco):
    if len(lista) >= 10:
        # o return sempre para a execução da função e retorna o valor
        return 'Atingido o número máximo de produtos'

    bebida = {'nome': nome, 'descricao': descricao, 'tipo': tipo, 'preco': preco}
    lista.append(bebida)
    return 'Produto cadastrado com sucesso!'

def listar(numero_elementos):
    if numero_elementos <= len(lista):
        return lista[:numero_elementos]
    return lista
