# Criar uma funcao para armazenar dados do carros 
# carro = marca, modelo
# funcao de salvar os dados em um arquivo csv
# dados devem ser separados por ;
# funcao deve usar a instrução with 
# cada carro deve ser salvo em uma linha

def salvar_carro(marca, modelo):
    with open('carros.csv', 'a') as arquivo:
        arquivo.write(f'{marca};{modelo}\n')
        