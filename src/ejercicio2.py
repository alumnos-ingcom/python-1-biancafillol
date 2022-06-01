"""Ejercicio 2
"""
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
        respuesta=1
    elif resultado==0:
        respuesta=0
    else:
        respuesta=-1
    return respuesta
def principal():
    """Esta función se encarga de la parte 'interactiva' del programa.
    """
    numero=float(input("Ingrese un número: "))
    resultado=signo(numero)
    print(resultado)
if __name__ == "__main__":
    principal()
