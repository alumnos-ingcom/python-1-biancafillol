"""Test del Ejercicio 11
"""
################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from src.ejercicio11 import es_multiplo
def test_es_multiplo_mayor_primero_positivos_false():
    """Esta función evalúa si es_multiplo funciona correctamente.
    """
    numero=8
    multiplo=2
    resultado=es_multiplo(numero, multiplo)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is False, "No se obtiene el resultado esperado."
def test_es_multiplo_mayor_segundo_positivos_true():
    """Esta función evalúa si es_multiplo funciona correctamente.
    """
    numero=3
    multiplo=9
    resultado=es_multiplo(numero, multiplo)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is True, "No se obtiene el resultado esperado."
def test_es_multiplo_mayor_segundo_positivos_false():
    """Esta función evalúa si es_multiplo funciona correctamente.
    """
    numero=2
    multiplo=7
    resultado=es_multiplo(numero, multiplo)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is False, "No se obtiene el resultado esperado."
def test_es_multiplo_iguales():
    """Esta función evalúa si es_multiplo funciona correctamente.
    """
    numero=2
    multiplo=2
    resultado=es_multiplo(numero, multiplo)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is True, "No se obtiene el resultado esperado."
def test_es_multiplo_ceros():
    """Esta función evalúa si es_multiplo funciona correctamente.
    """
    numero=0
    multiplo=0
    resultado=es_multiplo(numero, multiplo)
    assert isinstance(resultado, str), "El resultado debe ser un string."
def test_es_multiplo_negativos():
    """Esta función evalúa si es_multiplo funciona correctamente.
    """
    numero=-4
    multiplo=-8
    resultado=es_multiplo(numero, multiplo)
    assert isinstance(resultado, str), "El resultado debe ser un valor string."
def test_es_multiplo_negativo_primero():
    """Esta función evalúa si es_multiplo funciona correctamente.
    """
    numero=-3
    multiplo=-7
    resultado=es_multiplo(numero, multiplo)
    assert isinstance(resultado, str), "El resultado debe ser un valor string."
def test_es_multiplo_negativo_segundo():
    """Esta función evalúa si es_multiplo funciona correctamente.
    """
    numero=9
    multiplo=-32
    resultado=es_multiplo(numero, multiplo)
    assert isinstance(resultado, str), "El resultado debe ser un valor string."
def test_es_multiplo_iguales_negativos():
    """Esta función evalúa si es_multiplo funciona correctamente.
    """
    numero=-3
    multiplo=-3
    resultado=es_multiplo(numero, multiplo)
    assert isinstance(resultado, str), "El resultado debe ser un valor string."
