"""Test del Ejercicio 7
"""
################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from src.ejercicio7 import sexadecimal_a_decimal, decimal_a_sexadecimal
def test_a_decimal_positivos():
    """Esta función evalúa si sexadecimal_a_decimal funciona correctamente.
    """
    horas=9
    minutos=2
    segundos=5
    resultado=sexadecimal_a_decimal(horas, minutos, segundos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==32525, "No se obtiene el resultado esperado."
def test_a_decimal_ceros_segundos():
    """Esta función evalúa si sexadecimal_a_decimal funciona correctamente.
    """
    horas=12
    minutos=32
    segundos=0
    resultado=sexadecimal_a_decimal(horas, minutos, segundos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==45120, "No se obtiene el resultado esperado."
def test_a_decimal_ceros_minutos():
    """Esta función evalúa si sexadecimal_a_decimal funciona correctamente.
    """
    horas=4
    minutos=0
    segundos=56
    resultado=sexadecimal_a_decimal(horas, minutos, segundos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==14456, "No se obtiene el resultado esperado."
def test_a_decimal_ceros_horas():
    """Esta función evalúa si sexadecimal_a_decimal funciona correctamente.
    """
    horas=0
    minutos=43
    segundos=22
    resultado=sexadecimal_a_decimal(horas, minutos, segundos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==2602, "No se obtiene el resultado esperado."
def test_a_decimal_iguales():
    """Esta función evalúa si sexadecimal_a_decimal funciona correctamente.
    """
    horas=5
    minutos=5
    segundos=5
    resultado=sexadecimal_a_decimal(horas, minutos, segundos)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==18305, "No se obtiene el resultado esperado."
def test_decimal_a_sexadecimal_positivo():
    """Esta función evalúa si ecimal_a_sexadecimal funciona correctamente.
    """
    numero=354
    resultado=decimal_a_sexadecimal(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado==(0,5,54), "No se obtiene el resultado esperado."
def test_decimal_a_sexadecimal_cero():
    """Esta función evalúa si ecimal_a_sexadecimal funciona correctamente.
    """
    numero=0
    resultado=decimal_a_sexadecimal(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado==(0,0,0), "No se obtiene el resultado esperado."
def test_decimal_a_sexadecimal_menor_de_60():
    """Esta función evalúa si ecimal_a_sexadecimal funciona correctamente.
    """
    numero=32
    resultado=decimal_a_sexadecimal(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado==(0,0,32), "No se obtiene el resultado esperado."
def test_decimal_a_sexadecimal_mayor_de_60():
    """Esta función evalúa si ecimal_a_sexadecimal funciona correctamente.
    """
    numero=3661
    resultado=decimal_a_sexadecimal(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla."
    assert resultado==(1,1,1), "No se obtiene el resultado esperado."
