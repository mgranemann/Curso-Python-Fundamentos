# Criar arquivo novo - argumento 'a'
# Caso o arquivo já exista, ele adiciona o conteúdo ao final do arquivo existente
# Caso o arquivo não exista, ele será criado
from datetime import datetime

data_hora = datetime.now()

arquivo = open('arquivo3.txt', 'a')
arquivo.write(f'{data_hora}\n')
arquivo.close()
