# tratamento de excecao - try/except

import os


def deletar_arquivo(nome_arquivo):
    try:
        os.remove(nome_arquivo)        
    except:
        print('Arquivo não existe')

deletar_arquivo('placas.txt')