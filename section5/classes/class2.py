# Criar arquivo novo - argumento 'w'
# Caso o arquivo já exista, retorna sobrescreve o conteúdo
# Caso o arquivo não exista, ele será criado
arquivo = open('arquivo2.txt', 'w')
arquivo.write('Escrevendo dentro do arquivo existente')
arquivo.close()
