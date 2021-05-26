# Atividade 4 - Ler arquivo existente - argumento 'r'
# Cria uma funcao para ler as placas do arquivo criado pelo exercicio anterior
# A funcao deve retornar uma lista de strings onde cada elemento seja uma placa

def listar_placas():
    arquivo = open('placas.txt', 'r')
    lista = list(arquivo)
    arquivo.close()
    return lista

print(listar_placas())