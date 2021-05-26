# Crie uma funcao para listar os instrumentos salvos na atividade anterior
# A funcao deve converter cada linha em um dicionário, 
# A funcao deve tratar os caracteres de quebra de linha
# Caso ocorra algum erro durante a leitura, a funcao deve exibir a mensagem de erro (Exception)

def ler():
    try:
        lista_instrumentos = []
        with open('instrumentos.csv', 'x') as arquivo:
            for linha in arquivo:
                # funcao strip retira \n\t\r de uma string, espacos em branco antes e depois
                linha_limpa = linha.strip()
                lista_dados =  linha_limpa.split(';')
                instrumento = {'nome': lista_dados[0], 'descricao': lista_dados[1], 'valor':lista_dados[2] }
                lista_instrumentos.append(instrumento)
        return lista_instrumentos   
    except Exception as error:
        msg_erro = f'Não foi possivel ler o arquivo (nstrumentos.csv), verifique se ele existe'
        raise Exception(msg_erro)

try:
    lista = ler()
    for l in lista:
        print(l)
except Exception as e:
    print(e)
