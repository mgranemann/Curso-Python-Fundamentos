#funcoes

def soma(v1, v2):
    resultado = v1 + v2
    return resultado
# com valor padrao, chamado de opcional
def soma2(v1, v2, v3=0, v4=0):
    resultado = v1+ v2+ v3+ v4
    return  resultado

def soma3(v1, v2, v3=0, v4=0, v5=0):
    resultado = v1+ v2+ v3+ 2*(v4)+ v5
    return  resultado

def saudacao(nome):
    resultado = f'Olá, {nome}'
    return resultado

def retornos():
    num1 = 10
    num2 = 20
    return num1, num2

print( soma(10,20) )
print( saudacao('MDG') )

print( soma2(20,30,0,0) )
#chamada por paramentro nomeado
print( soma3(10, 15, v4=10) )

print(retornos())


