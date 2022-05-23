from plantilla import principal
################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
#PRECONDICIÓN: Ingresar dos números reales
#POSTCONDICIÓN: Obtener un -1, un 1, o un 0.
def compara(numero, otro_numero):
    """compara: Esta función suma y resta dos valores.
    Luego compara si el resultado de la suma es menor, mayor
    o igual al de la resta.
    """
    suma=numero + otro_numero
    resta=numero - otro_numero
    if suma<resta:
        print (-1)
    elif suma==resta:
        print (0)
    else:
        print (1)
compara(numero=float(input("Ingrese el primer número: ")),
otro_numero=float(input("Ingrese el segundo número: ")))
principal()
