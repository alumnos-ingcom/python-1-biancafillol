from plantilla import principal
################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
#PRECONDICIÓN: Ingresar un número real
#POSTCONDICIÓN: Obtener un número real con su indicación
#si es positivo(+), si es negativo(-) o si es neutro.
def signo(numero):
    """
    signo: Esta función se encarga de indicar si
    el número ingresado es positivo, negativo o neutro.
    """
    resultado= numero + numero
    if resultado>0:
        print (f"{resultado} es positivo (+).")
    elif resultado==0:
        print (f"{resultado} es neutro (N).")
    else:
        print (f"{resultado} es negativo (-).")
signo(numero=float(input("Ingrese un número: ")))
principal()
