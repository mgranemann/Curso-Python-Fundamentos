# importacao das pacotes do python ficam primeiro
import sys
# adiciona uma referencia a pasta atual, faz com que o 
#   python busque os arquivos nesta pasta
sys.path.append('.')

# . = pasta local
# .. = volta um nivel de pasta
# ../../ volta dois niveis de pasta

# importações das nossos pacotes ficam depois
# importação das funcoes cadastro e listar do mudulo class5_1  
from class5_1 import cadastrar, listar

# uso da função cadastrar do módulo class5_1  
msg = cadastrar('cerveja', 'puro malte', 18.5)
print(msg)


# uso da função listar do módulo class5_1  
for p in listar():
    print(p)