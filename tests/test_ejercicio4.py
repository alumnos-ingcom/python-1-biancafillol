"""Test del Ejercicio 4
"""
################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from src.ejercicio4 import suma_lenta
def test_suma_lenta_positivo():
    """Esta función evalúa si suma_lenta funciona correctamente.
    """
    numero_uno=6
    numero_dos=4
    resultado=suma_lenta(numero_uno, numero_dos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==10, "No se obtiene el resultado esperado."
def test_suma_lenta_negativo():
    """Esta función evalúa si suma_lenta funciona correctamente.
    """
    numero_uno=-4
    numero_dos=-9
    resultado=suma_lenta(numero_uno, numero_dos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==-13, "No se obtiene el resultado esperado."
def test_suma_lenta_negativo_primero():
    """Esta función evalúa si suma_lenta funciona correctamente.
    """
    numero_uno=-2
    numero_dos=1
    resultado=suma_lenta(numero_uno, numero_dos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==-1, "No se obtiene el resultado esperado."
def test_suma_lenta_negativo_segundo():
    """Esta función evalúa si suma_lenta funciona correctamente.
    """
    numero_uno=7
    numero_dos=-3
    resultado=suma_lenta(numero_uno, numero_dos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==4, "No se obtiene el resultado esperado."
def test_suma_lenta_cero():
    """Esta función evalúa si suma_lenta funciona correctamente.
    """
    numero_uno=0
    numero_dos=0
    resultado=suma_lenta(numero_uno, numero_dos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==0, "No se obtiene el resultado esperado."
def test_suma_lenta_iguales():
    """Esta función evalúa si suma_lenta funciona correctamente.
    """
    numero_uno=9
    numero_dos=9
    resultado=suma_lenta(numero_uno, numero_dos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==18, "No se obtiene el resultado esperado."
def test_suma_lenta_cero_primero():
    """Esta función evalúa si suma_lenta funciona correctamente.
    """
    numero_uno=0
    numero_dos=-3
    resultado=suma_lenta(numero_uno, numero_dos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==-3, "No se obtiene el resultado esperado."
def test_suma_lenta_cero_segundo():
    """Esta función evalúa si suma_lenta funciona correctamente.
    """
    numero_uno=2
    numero_dos=0
    resultado=suma_lenta(numero_uno, numero_dos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==2, "No se obtiene el resultado esperado."
def test_suma_lenta_iguales_resta_primero():
    """Esta función evalúa si suma_lenta funciona correctamente.
    """
    numero_uno=-11
    numero_dos=11
    resultado=suma_lenta(numero_uno, numero_dos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==0, "No se obtiene el resultado esperado."
def test_suma_lenta_iguales_resta_segundo():
    """Esta función evalúa si suma_lenta funciona correctamente.
    """
    numero_uno=12
    numero_dos=-12
    resultado=suma_lenta(numero_uno, numero_dos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==0, "No se obtiene el resultado esperado."
