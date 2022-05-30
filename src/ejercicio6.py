################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
#PRECONDICIÓN: Ingresar tres valores enteros.
#POSTCONDICIÓN: Obtener dos listas, una con los tres valores ordenados
#de mayor a menor, y la otra lista ordenados de menor a mayor.
def ordenar_mayor_a_menor(uno, dos, tres):
    """Esta función ordena en una lista los tres valores de mayor a menor.
    """
    if tres<uno>dos:
        if tres>dos:
            tupla=(uno,tres,dos)
        else:
            tupla=(uno,dos,tres)
    elif uno<tres>dos:
        if uno>dos:
            tupla=(tres,uno,dos)
        else:
            tupla=(tres,dos,uno)
    elif uno<dos>tres:
        if uno>tres:
            tupla=(dos,uno,tres)
        else:
            tupla=(dos,tres,uno)
    elif uno==dos==tres:
        tupla=(uno,dos, tres)
    respuesta_my_mn=tupla
    return respuesta_my_mn
def ordenar_menor_a_mayor(uno, dos, tres):
    """Esta función ordena en una lista los tres valores de menor a mayor.
    """
    if tres<uno>dos:
        if tres>dos:
            tupla=(dos,tres,uno)
        else:
            tupla=(tres,dos,uno)
    elif uno<tres>dos:
        if uno>dos:
            tupla=(dos,uno,tres)
        else:
            tupla=(uno,dos,tres)
    elif uno<dos>tres:
        if uno>tres:
            tupla=(tres,uno,dos)
        else:
            tupla=(uno,tres,dos)
    elif uno==dos==tres:
        tupla=(uno,dos, tres)
    respuesta_mn_my= tupla
    return respuesta_mn_my
def principal():
    """Esta función se encarga de la parte 'interactiva' del programa.
    """
    uno=int(input("Ingrese el primer valor: "))
    dos=int(input("Ingrese el segundo valor: "))
    tres=int(input("Ingrese el tercer valor: "))
    resultado_my=(ordenar_mayor_a_menor(uno, dos, tres))
    resultado_mn=(ordenar_menor_a_mayor(uno, dos, tres))
    print(f"De mayor a menor: {resultado_my}.")
    print(f"De menor a mayor: {resultado_mn}.")
if __name__ == "__main__":
    principal()
