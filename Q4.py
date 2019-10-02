############ Questao 4 ##############

n1 = int (input (" Entre com n1: "))
n2 = int (input (" Entre com n2: "))

def nob (n1, n2):

    n1 = str(n1)
    n2 = str(n2)

    valor1 = 0
    valor2 = 0

    for index1 in range (len(n1)):
        valor1 += int (n1 [index1])

    for index2 in range (len(n2)):
        valor2 += int (n2 [index2])

    resultado = valor1 + valor2

    return resultado

print (nob (n1, n2))

print (nob (21, 36))
