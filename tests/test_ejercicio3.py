"""Test del Ejercicio 3
"""
################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from src.ejercicio3 import compara
def test_compara_menor():
    """Esta función evalúa si compara funciona correctamente.
    """
    numero_uno=3
    numero_dos=6
    resultado=compara(numero_uno, numero_dos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==-1, "No se obtiene el resultado esperado."
def test_compara_mayor():
    """Esta función evalúa si compara funciona correctamente.
    """
    numero_uno=4
    numero_dos=2
    resultado=compara(numero_uno, numero_dos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==1, "No se obtiene el resultado esperado."
def test_compara_iguales():
    """Esta función evalúa si compara funciona correctamente.
    """
    numero_uno=8
    numero_dos=8
    resultado=compara(numero_uno, numero_dos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==0, "No se obtiene el resultado esperado."
