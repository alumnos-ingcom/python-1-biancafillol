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
    print(dividendo,end="")
    while dividendo>=divisor:
        print(f" - {divisor}",end="")
        dividendo=dividendo-divisor
        cociente=cociente+1
    resto=dividendo
    print(f" = {resto}")
    print(f"El cociente es: {cociente}")
    print(f"El resto es: {resto}")
def principal():
    """Esta función se encarga de la parte 'interactiva' del programa.
    """
    division_lenta(dividendo=int(input("Ingrese el dividendo: ")),
    divisor=int(input("Ingrese el divisor: ")))
if __name__ == "__main__":
    principal()
