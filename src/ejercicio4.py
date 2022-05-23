from plantilla import principal
################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
#PRECONDICIÓN: Ingresar dos números enteros.
#POSTCONDICIÓN: Obtener la suma lenta de los dos números enteros.
def suma_lenta(numero, otro_numero):
    """Esta función suma el primer número con el segundo número,
    (el segundo es separado por dígitos en 1 en 1).
    """
    print(numero,end="")
    if otro_numero>0:
        for otro in range(otro_numero):
            otro=1
            print(f" + {otro}",end="")
            numero=numero+1
        print(f" = {numero}")
    else:
        otro_numero=otro_numero*-1
        for otro in range(otro_numero):
            otro=1
            print(f" - {otro}",end="")
            numero=numero-1
        print(f" = {numero}")
suma_lenta(numero=int(input("Ingrese el primer número: ")),
otro_numero=int(input("Ingrese el segundo número: ")))
principal()
