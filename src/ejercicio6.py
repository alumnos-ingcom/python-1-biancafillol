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
    respuesta_my_mn=f"De mayor a menor: {lista}."
    return respuesta_my_mn
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
    respuesta_mn_my= f"De menor a mayor: {lista}."
    return respuesta_mn_my
def principal():
    """Esta función se encarga de la parte 'interactiva' del programa.
    """
    uno=int(input("Ingrese el primer valor: "))
    dos=int(input("Ingrese el segundo valor: "))
    tres=int(input("Ingrese el tercer valor: "))
    resultado_my=(ordenar_mayor_a_menor(uno, dos, tres))
    resultado_mn=(ordenar_menor_a_mayor(uno, dos, tres))
    print(resultado_my)
    print(resultado_mn)
if __name__ == "__main__":
    principal()
