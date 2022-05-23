################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
#PRECONDICIÓN: Ingresar un número decimal expresado en grados centigrados,
#e ingresar un número decimal expresado en grainput("Ingrese los grados fahrenheit: "))))
def principal():
    pass
if __name__ == "__main__":
    principal()dos fahrenheit.
#POSTCONDICIÓN: Obtener un número decimal expresado en grados fahrenheit,
#y obtener un número decimal expresado en grados centigrados.
def convertir_a_fahrenheit(centigrados):
    """
    convertir_a_fahrenheit: Esta función se encarga de convertir
    los grados centigrados a fahrenheit.
    """
    convertir_a_fahrenheit=((9*centigrados)/5)+32
    return "Convertidos a grados fahrenheit son: " + str(convertir_a_fahrenheit) + "° grados."
def convertir_a_centigrados(fahrenheit):
    """
    convertir_a_centigrados: Esta función se encarga de convertir
    los grados fahrenheit a grados centigrados.
    """
    convertir_a_centigrados=(5*(fahrenheit-32))/9
    return "Convertidos a grados centigrados son: " + str(convertir_a_centigrados) + "° grados."
print(convertir_a_fahrenheit(centigrados=float(input("Ingrese los grados centigrados: "))))
print(convertir_a_centigrados(fahrenheit=float(input("Ingrese los grados fahrenheit: "))))
def principal():
    pass
if __name__ == "__main__":
    principal()
