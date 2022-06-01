"""Test del Ejercicio N°1
"""
################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from src.ejercicio1 import convertir_a_fahrenheit, convertir_a_centigrados
def test_convertir_a_fahrenheit_positivo():
    """Esta función evalúa si convertir_a_fahrenheit funciona correctamente.
    """
    centigrados=23.3
    resultado=convertir_a_fahrenheit(centigrados)
    assert isinstance(resultado, float), "El resultado debe ser un número decimal."
    assert resultado==73.94, "No se obtiene el resultado esperado."
def test_convertir_a_fahrenheit_negativo():
    """Esta función evalúa si convertir_a_fahrenheit funciona correctamente.
    """
    centigrados=-44.2
    resultado=convertir_a_fahrenheit(centigrados)
    assert isinstance(resultado, float), "El resultado debe ser un número decimal."
    assert resultado==-47.56, "No se obtiene el resultado esperado."
def test_convertir_a_fahrenheit_cero():
    """Esta función evalúa si convertir_a_fahrenheit funciona correctamente.
    """
    centigrados=0.0
    resultado=convertir_a_fahrenheit(centigrados)
    assert isinstance(resultado, float), "El resultado debe ser un número decimal."
    assert resultado==32.0, "No se obtiene el resultado esperado."
def test_convertir_a_fahrenheit_negativo_a_positivo():
    """Esta función evalúa si convertir_a_fahrenheit funciona correctamente.
    """
    centigrados=-4.0
    resultado=convertir_a_fahrenheit(centigrados)
    assert isinstance(resultado, float), "El resultado debe ser un número decimal."
    assert resultado==24.8, "No se obtiene el resultado esperado."
def test_convertir_a_fahrenheit_iguales():
    """Esta función evalúa si convertir_a_fahrenheit funciona correctamente.
    """
    centigrados=-40.0
    resultado=convertir_a_fahrenheit(centigrados)
    assert isinstance(resultado, float), "El resultado debe ser un número decimal."
    assert resultado==-40.0, "No se obtiene el resultado esperado."
def test_convertir_a_centigrados_positivo():
    """Esta función evalúa si convertir_a_centigrados funciona correctamente.
    """
    fahrenheit=77.0
    resultado=convertir_a_centigrados(fahrenheit)
    assert isinstance(resultado, float), "El resultado debe ser un número decimal."
    assert resultado==25.0, "No se obtiene el resultado esperado."
def test_convertir_a_centigrados_negativo():
    """Esta función evalúa si convertir_a_centigrados funciona correctamente.
    """
    fahrenheit=-4.9
    resultado=convertir_a_centigrados(fahrenheit)
    assert isinstance(resultado, float), "El resultado debe ser un número decimal."
    assert resultado==-20.5, "No se obtiene el resultado esperado."
def test_convertir_a_centigrados_cero():
    """Esta función evalúa si convertir_a_centigrados funciona correctamente.
    """
    fahrenheit=0.0
    resultado=convertir_a_centigrados(fahrenheit)
    assert isinstance(resultado, float), "El resultado debe ser un número decimal."
    assert resultado==-17.77777777777778, "No se obtiene el resultado esperado."
def test_convertir_a_centigrados_positivo_a_negativo():
    """Esta función evalúa si convertir_a_centigrados funciona correctamente.
    """
    fahrenheit=4.0
    resultado=convertir_a_centigrados(fahrenheit)
    assert isinstance(resultado, float), "El resultado debe ser un número decimal."
    assert resultado==-15.555555555555555, "No se obtiene el resultado esperado."
def test_convertir_a_centigrados_iguales():
    """Esta función evalúa si convertir_a_fahrenheit funciona correctamente.
    """
    centigrados=-40.0
    resultado=convertir_a_fahrenheit(centigrados)
    assert isinstance(resultado, float), "El resultado debe ser un número decimal."
    assert resultado==-40.0, "No se obtiene el resultado esperado."
