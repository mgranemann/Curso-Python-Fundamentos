# tratamento generico - Exception as e

try:
    arquivo = open('a.txt', 'x')
except Exception as erro:
    print(f'Não foi possivel salvar!\nOcorreu um erro:{erro}')

arquivo = open('a.txt', 'x')