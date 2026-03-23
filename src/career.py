

## 🔹 1. career.py (REGRA DE NEGÓCIO)

def obter_habilidades_por_perfil(perfil):
    """
    Retorna habilidades recomendadas com base no perfil do usuário.
    """

    perfil = perfil.lower()

    if perfil == "iniciante":
        return ["Lógica de programação", "Git", "Python básico"]

    elif perfil == "transição":
        return ["Testes manuais", "QA", "Automação de testes", "Cypress"]

    elif perfil == "estudante":
        return ["Algoritmos", "Estrutura de dados", "Projetos práticos"]

    else:
        return ["Comunicação", "Resolução de problemas"]
