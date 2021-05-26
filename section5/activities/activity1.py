# Atividade 1 = Criar arquivo novo - argumento 'x'
# Crie uma funcao para salvar os sorteados de um premio
# A funcao deve receber o lista dos sorteados e o nome do premio por parametro
# A funcao deve salvar a lista dentro de um arquivo texto
# O arquivo texto deve ter o nome igual ao do premio
# Caso a funcao seja chamada novamente e o nome do arquivo seja o mesmo deve ocorre erro

def salvar_premiados(premiados, nome_premio):
    arquivo = open(f'{nome_premio}.txt','w')
    # arquivo.writelines(premiados)
    for s in premiados:
        arquivo.write(f'{s}\n')
    arquivo.close()

salvar_premiados(['bruno','william','luiz', 'maykon'], 'ferrari')