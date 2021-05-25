# Criar arquivo novo 
# para criar um novo - argumento 'x'
# arquivo = open('arquivo.txt', 'x')
# arquivo.write('Escrevendo dentro do arquivo')
# arquivo.close()

# Recricar o conteudo ('w')
# Se o arquivo nao existir, ele cria
# arquivo = open('arquivo2.txt', 'w')
# arquivo.write('Escrevendo dentro do arquivo existente')
# arquivo.close()

# Adicionar conteudo ao final
arquivo = open('arquivo3.txt', 'a')
arquivo.write('Escrevendo no final do arquivo\n')
arquivo.close()


# Ler um arquivo, ('r')
# com este argumento podemos apenas ler o arquivo
# e um arquivo em modo leitura transforma cada linha em um item de uma lista
arquivo = open('arquivo3.txt', 'r')
for linha in arquivo:
    print(linha)
arquivo.close()

print('---- limpa -----')

# limpar conteudo do arquivo
# a funcao strip() em uma string remove os espacos em branco do comece e final
#    e tambem remove todos os caracateres de escape \n \t \r
arquivo = open('arquivo3.txt', 'r')
for linha in arquivo:
    linha_limpa = linha.strip()
    print(linha_limpa)
arquivo.close()

# Ler dados em csv

# Remover arquivo

