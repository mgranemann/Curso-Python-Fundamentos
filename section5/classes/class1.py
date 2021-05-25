# Criar arquivo novo - argumento 'x'
# Caso o arquivo já exista, retorna erro
# Sempre que usarmos a função open(), devemos ao final usar a função close()
arquivo = open('arquivo1.txt', 'x')
arquivo.write('Escrevendo dentro do arquivo')
arquivo.close()
