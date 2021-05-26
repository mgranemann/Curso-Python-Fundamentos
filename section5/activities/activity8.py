# Crie uma funcao para remover arquivos
# o nome do arquivo deve ser recebido por parametro
# funcao deve retornar mensagem de sucesso
import os


def deletar_arquivo(nome_arquivo):
    os.remove(nome_arquivo)

deletar_arquivo('placas.txt')