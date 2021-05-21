#  Crie um procedimento que imprima:
#  Olá, dev
#  Curso de pyhton - fundamentos
#  Trabalhando com procedimento e funções

def imprimir():
    print('Olá, dev')
    print('Curso de pyhton - fundamentos')
    print('Trabalhando com procedimento e funções')

def imprimir2():
    mensagem = 'Olá, dev \nCurso de pyhton - fundamentos \nTrabalhando com procedimento e funções'
    print(mensagem)

def imprimir3():
    mensagem = '''
        Olá, dev 
        Curso de pyhton - fundamentos 
        Trabalhando com procedimento e funções
    '''
    print(mensagem)

imprimir()
imprimir2()
imprimir3()