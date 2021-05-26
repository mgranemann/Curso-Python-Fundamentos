# Atividade 6 -  Criando e lendo um arquivo CSV
# Crie uma funcao para cadastro de produtos
# funcao deve receber os dados do produto por parametro
# produto = nome, descricao e preco
# salvar em arquivo .csv separado por ;

# Crie uma funcao para ler produtos armazenados no arquivo csv
# funcao deve limpar os dados e converter de string para dicionario
# funcao de leitura deve retornar uma lista de dicionarios
# funcao nao deve imprimir

def salvar(nome, descricao, preco):
    arquivo = open('produtos.csv', 'a')
    arquivo.write(f"{nome};{descricao};{preco}\n")
    arquivo.close()

def listar():
    # abrindo arquivo de produtos
    arquivo = open('produtos.csv', 'r')
    # criando lista vazia para armazenar dicionarios de produtos
    lista = []
    for p in arquivo:
        # limpar linha
        linha_tratada = p.strip()
        # fatiar string pelo separador (;)
        dados = linha_tratada.split(';')
        # converter para dict
        produto = {'nome': dados[0], 'descricao': dados[1], 'preco': dados[2]}
        # adicionando elementos na lista
        lista.append(produto)
    # fechando arquivo
    arquivo.close()
    # retornado lista preenchida
    return lista