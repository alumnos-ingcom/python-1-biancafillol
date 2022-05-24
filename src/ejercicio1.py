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
    resultado_fah=((9*centigrados)/5)+32
    print (f"Convertidos a grados fahrenheit son: {resultado_fah}° grados.")
def convertir_a_centigrados(fahrenheit):
    """Esta función convierte los grados fahrenheit a centigrados."""
    resultado_centi=(5*(fahrenheit-32))/9
    print(f"Convertidos a grados fahrenheit son: {resultado_centi}° grados.")
convertir_a_fahrenheit(float(input("Ingrese los grados centigrados: ")))
convertir_a_centigrados(float(input("Ingrese los grados fahrenheit: ")))
def principal():
    pass

if __name__ == "__main__":
    principal()
