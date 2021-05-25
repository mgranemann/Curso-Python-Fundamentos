# Ler arquivo existente - argumento 'a'
# Caso o arquivo não exista, retorna erro
# Um arquivo em modo leitura é transformado em uma lista de string -
#   onde cada linha será um elemento da lista
arquivo = open('arquivo3.txt', 'r')
for linha in arquivo:
    print(linha)
arquivo.close()
