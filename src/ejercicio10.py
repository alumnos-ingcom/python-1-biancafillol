"""Ejercicio 10
"""
################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
#PRECONDICIÓN: Ingresar un string.
#POSTCONDICIÓN: Obtener un True o False.
def es_palindromo(texto):
    """Esta función determina si una palabra es un palíndromo o no.
    """
    texto= texto.lower()
    inicial=texto
    largo=0
    limite=len(texto)
    texto=list(texto)
    final=""
    while largo<limite:
        final=final + texto.pop()
        largo=largo+1
    respuesta= inicial==final
    return respuesta
def principal():
    """Esta función se encarga de la parte 'interactiva' del programa.
    """
    texto=input("Ingrese una palabra: ")
    resultado=es_palindromo(texto)
    print(resultado)
if __name__=="__main__":
    principal()
