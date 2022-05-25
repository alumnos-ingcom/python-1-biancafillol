################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
#PRECONDICIÓN: Ingresar un número entero.
#POSTCONDICIÓN: Obtener un valor booleano, True o False.
def es_primo(numero):
    """Esta función determina si un número es primo o no.
    """
    numero=abs(numero)
    divisores=0
    contador=1
    while contador<=numero:
        if numero%contador==0:
            divisores=divisores+1
        contador=contador + 1
    respuesta = bool(divisores==2)
    return respuesta
def principal():
    """Esta función se encarga de la parte 'interactiva' del programa.
    """
    numero=int(input("Ingrese un número: "))
    print(es_primo(numero))
if __name__ == "__main__":
    principal()
