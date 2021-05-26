# Atividade 2 - Criar arquivo novo - argumento 'w'
# Crie uma funcao para salvar uma lista de presenca
# a funcao deve receber a lista por parametro
# a funcao deve salvar a lista em arquivo texto
# o arquivo deve ter o nome de curso_python.txt
# a funcao pode ser chamada mais de uma vez para atualizar a lista

def salvar_presenca(lista):
    arquivo = open('curso_python.txt', 'w')
    for aluno in lista:
        arquivo.write(f'{aluno}\n')
    arquivo.close()


salvar_presenca(['Alessandro','Bruna', 'Bruno', 'Ximena'])