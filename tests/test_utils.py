
📄 testes/test_utils.py

from src.utils import formatar_lista


def test_lista_formatada():
    lista = ["Item 1", "Item 2"]
    resultado = formatar_lista(lista)
    
    assert "- Item 1" in resultado
    assert "- Item 2" in resultado


def test_lista_vazia():
    resultado = formatar_lista([])
    assert resultado == "Nenhum item encontrado"


def test_entrada_invalida():
    resultado = formatar_lista("texto")
    assert resultado == "Entrada inválida"
