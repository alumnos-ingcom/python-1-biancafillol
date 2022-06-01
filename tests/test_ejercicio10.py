"""Test del Ejercicio 10
"""
################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from src.ejercicio10 import es_palindromo
def test_es_palindromo_true():
    """Esta función evalúa si es_palindromo funciona correctamente.
    """
    texto="neuquen"
    resultado=es_palindromo(texto)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is True, "No se obtiene el resultado esperado."
def test_es_palindromo_false():
    """Esta función evalúa si es_palindromo funciona correctamente.
    """
    texto="hola"
    resultado=es_palindromo(texto)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is False, "No se obtiene el resultado esperado."
def test_es_palindromo_iguales():
    """Esta función evalúa si es_palindromo funciona correctamente.
    """
    texto="pppp"
    resultado=es_palindromo(texto)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is True, "No se obtiene el resultado esperado."
def test_es_palindromo_minuscula_true():
    """Esta función evalúa si es_palindromo funciona correctamente.
    """
    texto="rapar"
    resultado=es_palindromo(texto)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is True, "No se obtiene el resultado esperado."
def test_es_palindromo_mayuscula_true():
    """Esta función evalúa si es_palindromo funciona correctamente.
    """
    texto="OSO"
    resultado=es_palindromo(texto)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is True, "No se obtiene el resultado esperado."
def test_es_palindromo_minuscula_false():
    """Esta función evalúa si es_palindromo funciona correctamente.
    """
    texto="trabajo"
    resultado=es_palindromo(texto)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is False, "No se obtiene el resultado esperado."
def test_es_palindromo_mayuscula_false():
    """Esta función evalúa si es_palindromo funciona correctamente.
    """
    texto="PAPEL"
    resultado=es_palindromo(texto)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is False, "No se obtiene el resultado esperado."
def test_es_palindromo_minus_y_mayus_true():
    """Esta función evalúa si es_palindromo funciona correctamente.
    """
    texto="rEcoNOcER"
    resultado=es_palindromo(texto)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is True, "No se obtiene el resultado esperado."
def test_es_palindromo_minus_y_mayus_false():
    """Esta función evalúa si es_palindromo funciona correctamente.
    """
    texto="lApICeRa"
    resultado=es_palindromo(texto)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is False, "No se obtiene el resultado esperado."
def test_es_palindromo_iguaes_mayus():
    """Esta función evalúa si es_palindromo funciona correctamente.
    """
    texto="AAAAA"
    resultado=es_palindromo(texto)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is True, "No se obtiene el resultado esperado."
def test_es_palindromo_distintas_mayus():
    """Esta función evalúa si es_palindromo funciona correctamente.
    """
    texto="YOTUBE"
    resultado=es_palindromo(texto)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano."
    assert resultado is False, "No se obtiene el resultado esperado."
