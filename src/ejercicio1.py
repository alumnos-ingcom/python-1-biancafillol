################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
#PRECONDICIÓN: Ingresar un número decimal expresado en grados centigrados,
#e ingresar un número decimal expresado en grados fahrenheit.
#POSTCONDICIÓN: Obtener un número decimal expresado en grados fahrenheit,
#y obtener un número decimal expresado en grados centigrados.
def convertir_a_fahrenheit(centigrados):
    """Esta función convierte los grados centigrados a fahrenheit."""
    resultado_f=((9*centigrados)/5)+32
    return f"{centigrados}° centigrados convertidos a grados fahrenheit son: {resultado_f}° grados."
def convertir_a_centigrados(fahrenheit):
    """Esta función convierte los grados fahrenheit a centigrados."""
    resultado_c=(5*(fahrenheit-32))/9
    return f"{fahrenheit}° fahrenheit convertidos a grados centigrados son: {resultado_c}° grados."
def principal():
    """Esta función se encarga de la parte 'interactiva' del programa.
    """
    centigrados=float(input("Ingrese los grados centigrados: "))
    fahrenheit=float(input("Ingrese los grados fahrenheit: "))
    print(convertir_a_fahrenheit(centigrados))
    print(convertir_a_centigrados(fahrenheit))
if __name__ == "__main__":
    principal()
