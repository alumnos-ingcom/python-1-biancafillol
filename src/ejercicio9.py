"""Ejercicio 9
"""
################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
#PRECONDICIÓN: Ingresar un número entero positivo.
#POSTCONDICIÓN: Obtener la lista de los factores primos del número ingresado.
def factores_primos(numero):
    """Esta función descompone el número y ordena en una lista sus factores primos.
    """
    primo=2
    lista_factores_primos=[]
    while primo<=numero:
        while numero% primo==0:
            lista_factores_primos.append(primo)
            numero=numero/primo
        primo=primo+1
    respuesta= tuple(lista_factores_primos)
    return respuesta
def principal():
    """Esta función se encarga de la parte 'interactiva' del programa.
    """
    numero = int(input("Ingrese un número entero positivo: "))
    if numero>0:
        resultado=factores_primos(numero)
        print(f"Los factores primos de {numero} son: {resultado}")
    else:
        print("El número ingresado no es positivo, intentalo de nuevo.")
if __name__=="__main__":
    principal()
