# lancando excecao 'raise'
# Raise gera uma nova exceção e encaminha para quem chamou a execução

def dividir(num1, num2):
    try:
        resulta = num1 / num2
        return resulta
    except ZeroDivisionError:
        raise Exception('Não é permitido divisao por zero')

try:
    dividir(10,0)
except Exception as e: 
    print(e)