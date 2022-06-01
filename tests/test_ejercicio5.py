"""Test del Ejercicio 5
"""
################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from src.ejercicio5 import division_lenta
def test_division_lenta_positiva():
    """Esta función evalúa si division_lenta funciona correctamente.
    """
    dividendo=4
    divisor=2
    resultado=division_lenta(dividendo, divisor)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado[0]==2, "No se obtiene el resultado esperado."
    assert resultado[1]==0, "No se obtiene el resultado esperado."
def test_division_lenta_negativa():
    """Esta función evalúa si division_lenta funciona correctamente.
    """
    dividendo=-8
    divisor=-2
    resultado=division_lenta(dividendo, divisor)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado[0]==4, "No se obtiene el resultado esperado."
    assert resultado[1]==0, "No se obtiene el resultado esperado."
def test_division_lenta_ceros():
    """Esta función evalúa si division_lenta funciona correctamente.
    """
    dividendo=0
    divisor=0
    resultado=division_lenta(dividendo, divisor)
    assert isinstance(resultado, str), "El resultado debe ser un string."
def test_division_lenta_cero_primero():
    """Esta función evalúa si division_lenta funciona correctamente.
    """
    dividendo=0
    divisor=2
    resultado=division_lenta(dividendo, divisor)
    assert isinstance(resultado, str), "El resultado debe ser un string."
def test_division_lenta_cero_segundo():
    """Esta función evalúa si division_lenta funciona correctamente.
    """
    dividendo=7
    divisor=0
    resultado=division_lenta(dividendo, divisor)
    assert isinstance(resultado, str), "El resultado debe ser un string."
def test_division_lenta_negativo_primero():
    """Esta función evalúa si division_lenta funciona correctamente.
    """
    dividendo=-9
    divisor=3
    resultado=division_lenta(dividendo, divisor)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado[0]==-3, "No se obtiene el resultado esperado."
    assert resultado[1]==0, "No se obtiene el resultado esperado."
def test_division_lenta_negativo_segundo():
    """Esta función evalúa si division_lenta funciona correctamente.
    """
    dividendo=6
    divisor=-2
    resultado=division_lenta(dividendo, divisor)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado[0]==-3, "No se obtiene el resultado esperado."
    assert resultado[1]==0, "No se obtiene el resultado esperado."
def test_division_lenta_uno_segundo():
    """Esta función evalúa si division_lenta funciona correctamente.
    """
    dividendo=9
    divisor=1
    resultado=division_lenta(dividendo, divisor)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado[0]==9, "No se obtiene el resultado esperado."
    assert resultado[1]==0, "No se obtiene el resultado esperado."
def test_division_lenta_iguales():
    """Esta función evalúa si division_lenta funciona correctamente.
    """
    dividendo=22
    divisor=22
    resultado=division_lenta(dividendo, divisor)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado[0]==1, "No se obtiene el resultado esperado."
    assert resultado[1]==0, "No se obtiene el resultado esperado."
