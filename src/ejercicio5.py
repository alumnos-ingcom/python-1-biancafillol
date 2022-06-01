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
    inicial=dividendo, divisor
    dividendo=abs(dividendo)
    divisor=abs(divisor)
    if (inicial[0]<0 and inicial[1]<0) or (inicial[0]>0 and inicial[1]>0):
        if dividendo!=0:
            if divisor!=0:
                while dividendo>=divisor:
                    dividendo=dividendo-divisor
                    cociente=cociente+1
                resto=dividendo
                respuesta= cociente, resto
            else:
                respuesta="El divisor debe ser distinto de 0."
    elif inicial[0]<0 or inicial[1]<0:
        while dividendo>=divisor:
            dividendo=dividendo-divisor
            cociente=cociente+1
        resto=dividendo
        respuesta= (cociente*-1), (resto)
    else:
        respuesta="El cociente es 0 y el resto es 0."
    return respuesta
def principal():
    """Esta función se encarga de la parte 'interactiva' del programa.
    """
    dividendo=int(input("Ingrese el dividendo: "))
    divisor=int(input("Ingrese el divisor: "))
    resultado= division_lenta(dividendo, divisor)
    print(resultado)
if __name__ == "__main__":
    principal()
