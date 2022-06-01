"""Ejercicio 3
"""
################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
#PRECONDICIÓN: Ingresar dos números reales
#POSTCONDICIÓN: Obtener un -1, un 1, o un 0.
def compara(numero, otro_numero):
    """Esta función compara dos valores y determina si el primero es mayor, menor
    o igual al segundo valor.
    """
    suma_uno=numero + numero
    resta_uno=numero - otro_numero
    suma_dos=otro_numero + otro_numero
    resta_dos=otro_numero - otro_numero
    if suma_uno<suma_dos:
        resultado= -1
    elif resta_uno==resta_dos:
        resultado= 0
    else:
        resultado= 1
    return resultado
def principal():
    """Esta función se encarga de la parte 'interactiva' del programa.
    """
    numero=float(input("Ingrese el primer número: "))
    otro_numero= float(input("Ingrese el segundo número: "))
    respuesta=compara(numero, otro_numero)
    print(respuesta)
if __name__ == "__main__":
    principal()
