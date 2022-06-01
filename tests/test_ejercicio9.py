"""Test del Ejercicio 9
"""
################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from src.ejercicio9 import factores_primos
def test_factores_primos_positivo_tres_cifras():
    """Esta función evalúa si factores_primos funciona correctamente.
    """
    numero=128
    resultado=factores_primos(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado==(2,2,2,2,2,2,2), "No se obtiene el resultado esperado."
def test_factores_primos_minimo():
    """Esta función evalúa si factores_primos funciona correctamente.
    """
    numero=2
    resultado=factores_primos(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado==(2,), "No se obtiene el resultado esperado."
def test_factores_primos_uno():
    """Esta función evalúa si factores_primos funciona correctamente.
    """
    numero=1
    resultado=factores_primos(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado==(), "No se obtiene el resultado esperado."
def test_factores_primos_cero():
    """Esta función evalúa si factores_primos funciona correctamente.
    """
    numero=0
    resultado=factores_primos(numero)
    assert isinstance(resultado, str), "El resultado debe ser un string."
def test_factores_primos_unico():
    """Esta función evalúa si factores_primos funciona correctamente.
    """
    numero=5
    resultado=factores_primos(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado==(5,), "No se obtiene el resultado esperado."
def test_factores_primos_distintos():
    """Esta función evalúa si factores_primos funciona correctamente.
    """
    numero=14
    resultado=factores_primos(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado==(2,7), "No se obtiene el resultado esperado."
def test_factores_primos_tres_cifras_distinto():
    """Esta función evalúa si factores_primos funciona correctamente.
    """
    numero=305
    resultado=factores_primos(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado==(5,61), "No se obtiene el resultado esperado."
def test_factores_primos_negativo():
    """Esta función evalúa si factores_primos funciona correctamente.
    """
    numero=-4
    resultado=factores_primos(numero)
    assert isinstance(resultado, str), "El resultado debe ser un string."
def test_factores_primos_par_igual():
    """Esta función evalúa si factores_primos funciona correctamente.
    """
    numero=22
    resultado=factores_primos(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado==(2,11), "No se obtiene el resultado esperado."
def test_factores_primos_impar_igual():
    """Esta función evalúa si factores_primos funciona correctamente.
    """
    numero=11
    resultado=factores_primos(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado==(11,), "No se obtiene el resultado esperado."
def test_factores_primos_par_disntinto():
    """Esta función evalúa si factores_primos funciona correctamente.
    """
    numero=25
    resultado=factores_primos(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado==(5,5), "No se obtiene el resultado esperado."
def test_factores_primos_impardistinto():
    """Esta función evalúa si factores_primos funciona correctamente.
    """
    numero=91
    resultado=factores_primos(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado==(7,13), "No se obtiene el resultado esperado."
