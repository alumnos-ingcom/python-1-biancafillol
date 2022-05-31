"""Ejercicio 1
"""
import pytest
from src.ejercicio1 import convertir_a_fahrenheit, convertir_a_centigrados
def test_convertir_a_fahrenheit():
    """Esta función evalúa si convertir_a_fahrenheit funciona correctamente.
    """
    centigrados=23.3
    resultado=convertir_a_fahrenheit(centigrados)
    assert isinstance(resultado, float), "El resultado debe ser un número decimal."
    assert resultado==73.94, "No se obtiene el resultado esperado."
    return resultado
def test_convertir_a_centigrados():
    """Esta función evalúa si convertir_a_centigrados funciona correctamente.
    """
    fahrenheit=77.0
    resultado=convertir_a_centigrados(fahrenheit)
    assert isinstance(resultado, float), "El resultado debe ser un número decimal."
    assert resultado==25.0, "No se obtiene el resultado esperado."
