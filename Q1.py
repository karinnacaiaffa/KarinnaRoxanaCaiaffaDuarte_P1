########### Questao 1 ###########

a = int( input(" Entre com a!=0: "))
b = int( input(" Entre com b: "))
c = int( input(" Entre com c: "))

def raizes (a, b, c):

    delta = (b ** 2) - (4 * a * c)

    if (delta >= 0):
        raiz1 = (-b + ((delta) ** (1/2)))/(2 * a)
        raiz2 = (-b - ((delta) ** (1/2)))/(2 * a)
        print ("Raiz 1= ", raiz1, "e raiz 2= ", raiz2)
        return 0

    else:
        real= -b / (2 * a)
        imaginaria= ((delta) ** (1/2))/(2 * a)
        print ("Parte real=", real," e parte imaginaria=", imaginaria)
        return 1
    
    
raizes (a, b, c)

