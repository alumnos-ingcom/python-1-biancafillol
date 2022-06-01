"""Ejercicio 11
"""
################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
#PRECONDICIÓN: Ingresar dos números enteros positivos.
#POSTCONDICIÓN: Obtener un True o False.
def es_multiplo(numero, multiplo):
    """Esta función determina si el segundo número es múltiplo del primero.
    """
    mul=0
    if numero>0 and multiplo>0:
        while mul<multiplo:
            mul=mul+numero
        resultado= mul==multiplo
    else:
        resultado="No se ha ingresado un número positivo, intentelo de nuevo."
    return resultado
def principal():
    """Esta función se encarga de la parte 'interactiva' del programa.
    """
    numero=int(input("Ingrese un número entero positivo: "))
    multiplo=int(input("Ingrese un número entero positivo: "))
    respuesta=es_multiplo(numero, multiplo)
    print(respuesta)
if __name__=="__main__":
    principal()
