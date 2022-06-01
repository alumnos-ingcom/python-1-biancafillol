"""Test del Ejercicio 8
"""
################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from src.ejercicio8 import es_primo
def test_es_primo_positivo():
    """Esta función evalúa si es_primo funciona correctamente.
    """
    numero=4
    resultado=es_primo(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is False, "No se obtiene el resultado esperado."
def test_es_primo_negativo():
    """Esta función evalúa si es_primo funciona correctamente.
    """
    numero=-7
    resultado=es_primo(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is True, "No se obtiene el resultado esperado."
def test_es_primo_cero():
    """Esta función evalúa si es_primo funciona correctamente.
    """
    numero=0
    resultado=es_primo(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is False, "No se obtiene el resultado esperado."
def test_es_primo_uno():
    """Esta función evalúa si es_primo funciona correctamente.
    """
    numero=1
    resultado=es_primo(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is False, "No se obtiene el resultado esperado."
def test_es_primo_positivo_true():
    """Esta función evalúa si es_primo funciona correctamente.
    """
    numero=2
    resultado=es_primo(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is True, "No se obtiene el resultado esperado."
def test_es_primo_negativo_false():
    """Esta función evalúa si es_primo funciona correctamente.
    """
    numero=-8
    resultado=es_primo(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is False, "No se obtiene el resultado esperado."
