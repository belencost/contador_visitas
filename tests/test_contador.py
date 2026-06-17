import pytest
from src.contador import ContadorVisitas

def test_inicializacion():
    # Prueba que el contador arranque en cero
    c = ContadorVisitas()
    assert c.obtener_visitas() == 0

def test_incremento():
    # Prueba que sume de a uno correctamente
    c = ContadorVisitas()
    assert c.incrementar() == 1
    assert c.incrementar() == 2

def test_reiniciar():
    # Prueba que el botón de reinicio vuelva todo a cero
    c = ContadorVisitas()
    c.incrementar()
    c.reiniciar()
    assert c.obtener_visitas() == 0