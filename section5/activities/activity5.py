# Atividade 5 - Ler arquivo existente - argumento 'r' com funcao strip()
# Cria uma funcao para ler as placas do arquivo criado pelo exercicio 3
# A funcao deve retornar uma lista de strings onde cada elemento seja uma placa
# o dado nao deve conter nenhum caracter de escape ou espacos em brancos no inicio ou fim

def listar_placas():
    arquivo = open('placas.txt', 'r')
    lista = []
    for l in arquivo:
        lista.append(l.strip())
    arquivo.close()
    return lista

print(listar_placas())