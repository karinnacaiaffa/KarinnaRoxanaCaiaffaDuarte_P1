############### Questao 3 ##############

def pi (iteracoes):
    elem = 4
    while iteracoes > 1:
        denominator = (iteracoes * 2) - 1
        if iteracoes % 2 == 0:
            elem -= (4 / denominator)
        else:
            elem += (4 / denominator)
        iteracoes -= 1
    return elem

def main():
    iteracoes = 1
    print ("Valor de PI com 5x10e-4: ")
    while abs ( pi (iteracoes + 1)- pi (iteracoes) ) > 5e-4:
        iteracoes += 1
    print("Número de iteracoes: ", iteracoes)
    print("Valor de PI: ", pi (iteracoes + 1))

main()
