# tratamento especifico - ValueError 
try:
    arquivo = open('a4.txt', 'x')
    resultado = 10/1
    teste = int('asdasdas')
except FileExistsError:
    print(f'Não foi possivel salvar')
except ZeroDivisionError:
    print('Nao foi é possivel dividir por zero')
except Exception as error:
    print(type(error))

