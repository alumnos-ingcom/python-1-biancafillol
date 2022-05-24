################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
#PRECONDICIÓN: Ingresar dos números enteros.
#POSTCONDICIÓN: Obtener el resultado de la suma lenta de los dos números.
def suma_lenta(numero, otro_numero):
    """Esta función suma el primer número con el segundo número,
    (el segundo es separado por dígitos en 1 en 1).
    """
    contador=0
    print(numero,end="")
    while contador<abs(otro_numero):
        if otro_numero>0:
            print(" + 1",end="")
            numero=numero+1
        else:
            print(" - 1",end="")
            numero=numero-1
        contador=contador+1
    print(f" = {numero}")
def principal():
    """Esta función se encarga de la parte 'interactiva' del programa.
    """
    numero=int(input("Ingrese el primer número: "))
    otro_numero=int(input("Ingrese el segundo número: "))
    return suma_lenta(numero, otro_numero)
if __name__ == "__main__":
    principal()
