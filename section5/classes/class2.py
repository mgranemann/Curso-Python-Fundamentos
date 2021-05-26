# Criar arquivo novo - argumento 'w'
# Caso o arquivo já exista, retorna sobrescreve o conteúdo
# Caso o arquivo não exista, ele será criado
from datetime import datetime

data_hora = datetime.now()
arquivo = open(f'{data_hora}.txt', 'w')
arquivo.write('Carro1\n')
arquivo.close()
