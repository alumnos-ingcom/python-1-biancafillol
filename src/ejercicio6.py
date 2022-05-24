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
            lista=[uno,tres,dos]
        else:
            lista=[uno,dos,tres]
    elif uno<tres>dos:
        if uno>dos:
            lista=[tres,uno,dos]
        else:
            lista=[tres,dos,uno]
    elif uno<dos>tres:
        if uno>tres:
            lista=[dos,uno,tres]
        else:
            lista=[dos,tres,uno]
    elif uno==dos==tres:
        lista=[uno,dos, tres]
    return f"De mayor a menor: {lista}."
def ordenar_menor_a_mayor(uno, dos, tres):
    """Esta función ordena en una lista los tres valores de menor a mayor.
    """
    if tres<uno>dos:
        if tres>dos:
            lista=[dos,tres,uno]
        else:
            lista=[tres,dos,uno]
    elif uno<tres>dos:
        if uno>dos:
            lista=[dos,uno,tres]
        else:
            lista=[uno,dos,tres]
    elif uno<dos>tres:
        if uno>tres:
            lista=[tres,uno,dos]
        else:
            lista=[uno,tres,dos]
    elif uno==dos==tres:
        lista=[uno,dos, tres]
    return f"De menor a mayor: {lista}."
def principal():
    """Esta función se encarga de la parte 'interactiva' del programa.
    """
    uno=int(input("Ingrese el primer valor: "))
    dos=int(input("Ingrese el segundo valor: "))
    tres=int(input("Ingrese el segundo valor: "))
    print(ordenar_mayor_a_menor(uno, dos, tres))
    print(ordenar_menor_a_mayor(uno, dos, tres))
if __name__ == "__main__":
    principal()
