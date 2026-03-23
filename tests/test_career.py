
📄 testes/test_career.py


from src.career import obter_habilidades_por_perfil


def test_perfil_iniciante():
    resultado = obter_habilidades_por_perfil("iniciante")
    assert "Python básico" in resultado


def test_perfil_transicao():
    resultado = obter_habilidades_por_perfil("transição")
    assert "QA" in resultado


def test_perfil_estudante():
    resultado = obter_habilidades_por_perfil("estudante")
    assert "Algoritmos" in resultado


def test_perfil_invalido():
    resultado = obter_habilidades_por_perfil("qualquer coisa")
    assert "Comunicação" in resultado
