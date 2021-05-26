# tratamento de excecao - try/except

import os


def deletar_arquivo(nome_arquivo):
    try:
        # caso algum erro ocorra,
        # será encaminhado para o bloco except
        os.remove(nome_arquivo)        
    except:
        #trata os erros ocorridos no bloco try
        print('Arquivo não existe')

deletar_arquivo('placas.txt')