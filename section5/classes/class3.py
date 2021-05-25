# Criar arquivo novo - argumento 'a'
# Caso o arquivo já exista, ele adiciona o conteúdo ao final do arquivo existente
# Caso o arquivo não exista, ele será criado
arquivo = open('arquivo3.txt', 'a')
arquivo.write('Escrevendo no final do arquivo\n')
arquivo.close()
