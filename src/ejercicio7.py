"""Ejercicio 7
"""
################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
#PRECONDICIÓN: Ingresar tres números enteros positivos expresados en horas,
#minutos y segundos.
#POSTCONDICIÓN: Obtener la cantidad total de segundos y la expresión de estos
#en horas, minutos y segundos en una lista.
def sexadecimal_a_decimal(horas, minutos, segundos):
    """Esta función convierte las horas, minutos y segundos a segundos.
    """
    minutos=minutos+(horas*60)
    resp=segundos+(minutos*60)
    return resp
def decimal_a_sexadecimal(numero):
    """Esta función convierte los segundos a horas, minutos y segundos.
    """
    horas_n= (numero //60)//60
    minutos_n=(numero//60)%60
    segundos_n=numero%60
    respuest= (horas_n, minutos_n, segundos_n)
    return respuest
def principal():
    """Esta función se encarga de la parte 'interactiva' del programa.
    """
    horas=int(input("Ingrese las horas: "))
    minutos=int(input("Ingrese los minutos: "))
    segundos=int(input("Ingrese los segundos: "))
    numero=sexadecimal_a_decimal(horas, minutos, segundos)
    resultado=decimal_a_sexadecimal(numero)
    print(f"En total son {numero} segundos.")
    print(f"{numero} segundos es equivalente a: {resultado}.")
if __name__ == "__main__":
    principal()
