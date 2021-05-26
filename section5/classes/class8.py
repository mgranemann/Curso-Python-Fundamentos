# instrução with - fechamento automatico do recurso

arquivo = open('teste.txt', 'x')
arquivo.write('testando...')
arquivo.close()

with open('teste2.txt', 'x') as arquivo:
    arquivo.write('testando...')
