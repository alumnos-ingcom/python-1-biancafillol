"""Ejercicio 5
"""
################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
#PRECONDICIÓN: Ingresar dos números enteros.
#POSTCONDICIÓN: Obtener el cociente y el resto mediante resta sucesiva.
def division_lenta(dividendo, divisor):
    """Esta función hace que el dividendo sea restado sucevisamente
    por el divisor hasta que el resultado de menor o igual al dividendo.
    """
    cociente=0
    while dividendo>=divisor:
        dividendo=dividendo-divisor
        cociente=cociente+1
    resto=dividendo
    respuesta= cociente, resto
    return respuesta
def principal():
    """Esta función se encarga de la parte 'interactiva' del programa.
    """
    dividendo=int(input("Ingrese el dividendo: "))
    divisor=int(input("Ingrese el divisor: "))
    if dividendo>0:
        if divisor>0:
            resultado= division_lenta(dividendo, divisor)
            print(f"El cociente es {resultado[0]} y el resto es {resultado[1]}.")
        else:
            dividendo=abs(dividendo)
            divisor=abs(divisor)
            resultado= division_lenta(dividendo, divisor)
            print(f"El cociente es -{resultado[0]} y el resto es {resultado[1]}.")
    elif dividendo==0:
        if divisor==0:
            print("El divisor debe ser distinto de 0.")
        else:
            print("El cociente es 0 y el resto es 0.")
    elif divisor==0:
        if dividendo==0:
            print("El divisor debe ser distinto de 0.")
        else:
            print("El divisor debe ser distinto de 0.")
    else:
        dividendo=abs(dividendo)
        if divisor>0:
            resultado= division_lenta(dividendo, divisor)
            print(f"El cociente es -{resultado[0]} y el resto es {resultado[1]}.")
        else:
            divisor=abs(divisor)
            resultado= division_lenta(dividendo, divisor)
            print(f"El cociente es {resultado[0]} y el resto es {resultado[1]}.")
if __name__ == "__main__":
    principal()
