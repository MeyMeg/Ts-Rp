from app import soma, subtrai, multiplica, divide, saudacao
import pytest

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0

def test_subtrai():
    assert subtrai(10, 4) == 6
    assert subtrai(0, 3) == -3

def test_multiplica():
    assert multiplica(2, 5) == 10
    assert multiplica(-1, 3) == -3

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    with pytest.raises(ValueError):
        divide(5, 0)

def test_saudacao():
    assert saudacao("Maria") == "Olá, Maria! Bem-vindo(a) à disciplina."
    assert "disciplina" in saudacao("Maria")
