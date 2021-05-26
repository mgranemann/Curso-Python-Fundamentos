# tratamento generico - Exception as e

try:
    arquivo = open('a.txt', 'x')
except Exception as erro:
    print(f'\n\n\nNão foi possivel salvar!\nOcorreu um erro:{erro}\n\n\n')


arquivo = open('a.txt', 'x')