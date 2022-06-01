"""Test del Ejercicio 6
"""
################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from src.ejercicio6 import ordenar_mayor_a_menor, ordenar_menor_a_mayor
def test_myr_a_mnr_1_3_2():
    """Esta función evalúa si ordenar_mayor_a_menor funciona correctamente.
    """
    uno=9
    dos=2
    tres=5
    resultado=ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado==(9,5,2), "No se obtiene el resultado esperado."
def test_myr_a_mnr_1_2_3():
    """Esta función evalúa si ordenar_mayor_a_menor funciona correctamente.
    """
    uno=2
    dos=0
    tres=-1
    resultado=ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado==(2,0,-1), "No se obtiene el resultado esperado."
def test_myr_a_mnr_3_1_2():
    """Esta función evalúa si ordenar_mayor_a_menor funciona correctamente.
    """
    uno=13
    dos=7
    tres=22
    resultado=ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado==(22,13,7), "No se obtiene el resultado esperado."
def test_myr_a_mnr_3_2_1():
    """Esta función evalúa si ordenar_mayor_a_menor funciona correctamente.
    """
    uno=-21
    dos=21
    tres=43
    resultado=ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado==(43,21,-21), "No se obtiene el resultado esperado."
def test_myr_a_mnr_2_1_3():
    """Esta función evalúa si ordenar_mayor_a_menor funciona correctamente.
    """
    uno=-8
    dos=2
    tres=-32
    resultado=ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado==(2,-8,-32), "No se obtiene el resultado esperado."
def test_myr_a_mnr_2_3_1():
    """Esta función evalúa si ordenar_mayor_a_menor funciona correctamente.
    """
    uno=0
    dos=2
    tres=10
    resultado=ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado==(10,2,0), "No se obtiene el resultado esperado."
def test_myr_a_mnr_iguales():
    """Esta función evalúa si ordenar_mayor_a_menor funciona correctamente.
    """
    uno=23
    dos=23
    tres=23
    resultado=ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado==(23,23,23), "No se obtiene el resultado esperado."
def test_myr_a_mnr_ceros():
    """Esta función evalúa si ordenar_mayor_a_menor funciona correctamente.
    """
    uno=0
    dos=0
    tres=0
    resultado=ordenar_mayor_a_menor(uno, dos, tres)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado==(0,0,0), "No se obtiene el resultado esperado."
def test_mnr_a_myr_2_3_1():
    """Esta función evalúa si ordenar_menor_a_mayor funciona correctamente.
    """
    uno=3
    dos=0
    tres=8
    resultado=ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado==(0,3,8), "No se obtiene el resultado esperado."
def test_mnr_a_myr_3_2_1():
    """Esta función evalúa si ordenar_menor_a_mayor funciona correctamente.
    """
    uno=0
    dos=-1
    tres=-4
    resultado=ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado==(-4,-1,0), "No se obtiene el resultado esperado."
def test_mnr_a_myr_2_1_3():
    """Esta función evalúa si ordenar_menor_a_mayor funciona correctamente.
    """
    uno=23
    dos=3
    tres=56
    resultado=ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado==(3,23,56), "No se obtiene el resultado esperado."
def test_mnr_a_myr_1_2_3():
    """Esta función evalúa si ordenar_menor_a_mayor funciona correctamente.
    """
    uno=3
    dos=6
    tres=84
    resultado=ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado==(3,6,84), "No se obtiene el resultado esperado."
def test_mnr_a_myr_1_3_2():
    """Esta función evalúa si ordenar_menor_a_mayor funciona correctamente.
    """
    uno=6
    dos=12
    tres=24
    resultado=ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado==(6,12,24), "No se obtiene el resultado esperado."
def test_mnr_a_myr_iguales():
    """Esta función evalúa si ordenar_menor_a_mayor funciona correctamente.
    """
    uno=56
    dos=56
    tres=56
    resultado=ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado==(56,56,56), "No se obtiene el resultado esperado."
def test_mnr_a_myr_ceros():
    """Esta función evalúa si ordenar_menor_a_mayor funciona correctamente.
    """
    uno=0
    dos=0
    tres=0
    resultado=ordenar_menor_a_mayor(uno, dos, tres)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado==(0,0,0), "No se obtiene el resultado esperado."
