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
        respuesta=f"{numero} es positivo (+)."
    elif resultado==0:
        respuesta=f"{numero} es neutro (N)."
    else:
        respuesta=f"{numero} es negativo (-)."
    return respuesta
def principal():
    """Esta función se encarga de la parte 'interactiva' del programa.
    """
    numero=float(input("Ingrese un número: "))
    print(signo(numero))
if __name__ == "__main__":
    principal()
