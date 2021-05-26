# Atividade 3 - Criar arquivo novo - argumento 'a'
# Crie uma funcao para salvar uma placa de veiculo
# A funcao deve receber a placa por parametro
# A funcao deverá armazenar em arquivo texto
# cada placa deve ser armazenada em uma linha

def estacionamento(placa):
    arquivo = open('placas.txt', 'a')
    arquivo.write(f'{placa}\n')
    arquivo.close()

estacionamento('MMM-0909')