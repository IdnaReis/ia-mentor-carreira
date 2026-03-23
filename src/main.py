
🔹 3.  (ORQUESTRAÇÃO)

from career import obter_habilidades_por_perfil
from utils import formatar_lista


def executar():
    print("🚀 IA Mentor de Carreira\n")

    perfil = input("Digite seu perfil (iniciante, estudante, transição): ")

    habilidades = obter_habilidades_por_perfil(perfil)

    print("\n💡 Sugestões de habilidades:\n")
    print(formatar_lista(habilidades))


if __name__ == "__main__":
    executar()
