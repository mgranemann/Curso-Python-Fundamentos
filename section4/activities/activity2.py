# Exercicios funcoes
# Crie uma calculadora com as quatro operacoes basicas (soma, sub, multi, div)
# cada operação deve ser uma funcao
# as funcoes devem receber dois valores inteiros e retornar o resultado da operacao
# para a divisao, a funcao nao deve permitir divisao por zero

# https://github.com/mgranemann/ 

def soma(n1, n2):
    resultado = n1 + n2
    return resultado

def subt(n1, n2):
    resultado = n1 - n2
    return resultado

def mult(n1, n2):
    resultado = n1 * n2
    return resultado

def divi(n1, n2):
    resultado = None
    if n2 == 0:
        print('Não é possivel dividir por zero')
    else:
        resultado = n1 / n2

    return resultado

v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))

print(soma(v1, v2))
print(subt(v1, v2))
print(mult(v1, v2))
print(divi(v1, v2))