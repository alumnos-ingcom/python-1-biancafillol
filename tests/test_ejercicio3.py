"""Test del Ejercicio 3
"""
################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from src.ejercicio3 import compara
def test_compara_menor_positivo():
    """Esta función evalúa si compara funciona correctamente.
    """
    numero_uno=3
    numero_dos=6
    resultado=compara(numero_uno, numero_dos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==-1, "No se obtiene el resultado esperado."
def test_compara_mayor_positivo():
    """Esta función evalúa si compara funciona correctamente.
    """
    numero_uno=4
    numero_dos=2
    resultado=compara(numero_uno, numero_dos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==1, "No se obtiene el resultado esperado."
def test_compara_iguales_positivos():
    """Esta función evalúa si compara funciona correctamente.
    """
    numero_uno=8
    numero_dos=8
    resultado=compara(numero_uno, numero_dos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==0, "No se obtiene el resultado esperado."
def test_compara_ceros():
    """Esta función evalúa si compara funciona correctamente.
    """
    numero_uno=0
    numero_dos=0
    resultado=compara(numero_uno, numero_dos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==0, "No se obtiene el resultado esperado."
def test_compara_mayor_negativo():
    """Esta función evalúa si compara funciona correctamente.
    """
    numero_uno=-1
    numero_dos=-3
    resultado=compara(numero_uno, numero_dos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==1, "No se obtiene el resultado esperado."
def test_compara_menor_negativo():
    """Esta función evalúa si compara funciona correctamente.
    """
    numero_uno=-23
    numero_dos=-21
    resultado=compara(numero_uno, numero_dos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==-1, "No se obtiene el resultado esperado."
def test_compara_iguales_negativos():
    """Esta función evalúa si compara funciona correctamente.
    """
    numero_uno=-4
    numero_dos=-4
    resultado=compara(numero_uno, numero_dos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==0, "No se obtiene el resultado esperado."
def test_compara_cero_primero_positivo():
    """Esta función evalúa si compara funciona correctamente.
    """
    numero_uno=0
    numero_dos=1
    resultado=compara(numero_uno, numero_dos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==-1, "No se obtiene el resultado esperado."
def test_compara_cero_primero_negativo():
    """Esta función evalúa si compara funciona correctamente.
    """
    numero_uno=0
    numero_dos=-11
    resultado=compara(numero_uno, numero_dos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==1, "No se obtiene el resultado esperado."
def test_compara_cero_segundo_positivo():
    """Esta función evalúa si compara funciona correctamente.
    """
    numero_uno=4
    numero_dos=0
    resultado=compara(numero_uno, numero_dos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==1, "No se obtiene el resultado esperado."
def test_compara_cero_segundo_negativo():
    """Esta función evalúa si compara funciona correctamente.
    """
    numero_uno=-5
    numero_dos=0
    resultado=compara(numero_uno, numero_dos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==-1, "No se obtiene el resultado esperado."

