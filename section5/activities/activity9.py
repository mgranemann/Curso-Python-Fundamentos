# Criar um funcao para salvar instrumentos musicais
# instrumento =  nome, descricao, valor
# os dados do instrumento serao recebidos por parametro
# os dados devem ser salvos em arquivo texto
# cada instrumento deve ser salvo em 1 linha dirente
# os dados devem ser separados por ; (arquivo.csv)
# Usar tratamento de excecao
# Caso o dado seja salva com sucesso = 'Instrumento salvo com sucesso!'
# Caso ocorra algum erro mensagem = 'Nao foi possivel salvar!'

def salvar(nome, descricao, valor):
    try:
        with open('instrumentos.csv', 'a') as arquivo:
            arquivo.write( f'{nome};{descricao};{valor}\n' )
        return 'Instrumento salvo com sucesso!'
    except:
        return 'Não foi possivel salvar!'


try:
    msg = salvar('Bateria', 'Da Proway', 1000.00)
    print(msg)
except:
    print('Erro desconhecido')