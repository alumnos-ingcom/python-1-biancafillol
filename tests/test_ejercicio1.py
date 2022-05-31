"""Test del Ejercicio N°1
"""
import pytest
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
