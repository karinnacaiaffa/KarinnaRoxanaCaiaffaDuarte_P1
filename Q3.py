############### Questao 3 ##############

pi = 0
divisor = 1
razao = 1
aux = 1

while (razao > (5 * 10 ** (-8))) or (razao != (5 * 10 ** (-8))):
    anterior = pi
    pi = pi + 4/ (divisor * aux)
    divisor += 2
    aux *= -1

    razao = (anterior - pi) * aux

    print (pi)
~                                                                                                                                             
~                          
