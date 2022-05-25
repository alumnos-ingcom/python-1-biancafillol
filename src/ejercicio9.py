################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
#PRECONDICIÓN: Ingresar un número entero positivo.
#POSTCONDICIÓN: Obtener la lista de los factores primos del número ingresado.
def factores_primos(numero):
    """Esta función descompone el número y ordena en una lista sus factores primos.
    """
    if numero>0:
        num=numero
        primo=2
        lista_factores_primos=[]
        while primo<=numero:
            while numero% primo==0:
                lista_factores_primos.append(primo)
                numero=numero/primo
            primo=primo+1
        respuesta= f"Los factores primos de {num} son: {lista_factores_primos}. "
    else:
        respuesta= "El número ingresado no es positivo, intentalo de nuevo."
    return respuesta
def principal():
    """Esta función se encarga de la parte 'interactiva' del programa.
    """
    numero = int(input("Ingrese un número entero positivo: "))
    print(factores_primos(numero))
if __name__=="__main__":
    principal()
