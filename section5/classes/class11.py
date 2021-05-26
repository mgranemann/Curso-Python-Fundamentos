# tratamento especifico - ValueError 
try:
    arquivo = open('a2.txt', 'x')
    resultado = 10/0
except FileExistsError as error1:
    print(f'Não foi possivel salvar!\nOcorreu um erro:{error1}')
except Exception as error2:
    print(f'Não foi possivel dividir!\nOcorreu um erro:{error2}')

