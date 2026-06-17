import pytest
from src.contador import ContadorClics

def test_inicializacion():
    # Prueba que el contador arranque en cero
    c = ContadorClics()
    assert c.obtener_clics() == 0

def test_incremento():
    # Prueba que sume de a uno correctamente
    c = ContadorClics()
    assert c.incrementar() == 1
    assert c.incrementar() == 2

def test_reiniciar():
    # Prueba que el botón de reinicio vuelva todo a cero
    c = ContadorClics()
    c.incrementar()
    c.reiniciar()
    assert c.obtener_clics() == 0