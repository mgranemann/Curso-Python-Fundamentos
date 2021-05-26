# Criando um arquivo CSV
carro = {'marca': 'hyundai', 'modelo':'i30', 'motorizacao': 2.0}

arquivo = open('carros.csv', 'a')
arquivo.write(f'{carro["marca"]};{carro["modelo"]};{carro["motorizacao"]}\n')
arquivo.close()

# Ler dados em csv
arquivo = open('carros.csv', 'r')
for linha in arquivo:
    linha_tratada = linha.strip()
    carro_lista = linha_tratada.split(';')
    carro = {'marca': carro_lista[0], 'modelo':carro_lista[1], 'motorizacao': carro_lista[2]}
    print(carro)
arquivo.close()