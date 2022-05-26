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
    respuesta= f"El cociente es {cociente} y el resto es {resto}."
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
