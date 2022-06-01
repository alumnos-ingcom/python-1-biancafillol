"""Test del Ejercicio N°2
"""
################
# Bianca Fillol - @bianfillol
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from src.ejercicio2 import signo
def test_signo_negativo():
    """Esta función evalúa si signo funciona correctamente
    cuando el número es negativo.
    """
    numero=-6.2
    resultado=signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==-1, "No se obtiene el resultado esperado."
def test_signo_positivo():
    """Esta función evalúa si signo funciona correctamente
    cuando el número es positivo.
    """
    numero=3.9
    resultado=signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==1, "No se obtiene el resultado esperado."
def test_signo_neutro():
    """Esta función evalúa si signo funciona correctamente
    cuando el número es nuetro.
    """
    numero=0
    resultado=signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==0, "No se obtiene el resultado esperado."
def test_signo_cero_positivo():
    """Esta función evalúa si signo funciona correctamente
    cuando el número es nuetro.
    """
    numero=0.5
    resultado=signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==1, "No se obtiene el resultado esperado."
def test_signo_cero_negativo():
    """Esta función evalúa si signo funciona correctamente
    cuando el número es nuetro.
    """
    numero=-0.12
    resultado=signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==-1, "No se obtiene el resultado esperado."
def test_signo_uno():
    """Esta función evalúa si signo funciona correctamente
    cuando el número es nuetro.
    """
    numero=1
    resultado=signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==1, "No se obtiene el resultado esperado."
def test_signo_entero_positivo():
    """Esta función evalúa si signo funciona correctamente
    cuando el número es nuetro.
    """
    numero=9
    resultado=signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==1, "No se obtiene el resultado esperado."
def test_signo_entero_negativo():
    """Esta función evalúa si signo funciona correctamente
    cuando el número es nuetro.
    """
    numero=-5
    resultado=signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==-1, "No se obtiene el resultado esperado."
def test_signo_par_positivo():
    """Esta función evalúa si signo funciona correctamente
    cuando el número es nuetro.
    """
    numero=42
    resultado=signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==1, "No se obtiene el resultado esperado."
def test_signo_par_negativo():
    """Esta función evalúa si signo funciona correctamente
    cuando el número es nuetro.
    """
    numero=-80
    resultado=signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==-1, "No se obtiene el resultado esperado."
def test_signo_impar_positivo():
    """Esta función evalúa si signo funciona correctamente
    cuando el número es nuetro.
    """
    numero=7
    resultado=signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==1, "No se obtiene el resultado esperado."
def test_signo_impar_negativo():
    """Esta función evalúa si signo funciona correctamente
    cuando el número es nuetro.
    """
    numero=13
    resultado=signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado==1, "No se obtiene el resultado esperado."
