import math
import json

UNIDADES_PERMITIDAS = ["cm", "l"]

class Cilindro:
    def __init__(self, nome, unidade, altura, raio):
        if unidade not in UNIDADES_PERMITIDAS:
            raise ValueError(f"Unidade inválida: '{unidade}'. Use apenas {UNIDADES_PERMITIDAS}.")

        self.nome = nome
        self.unidade = unidade
        self.altura = altura
        self.raio = raio

    def volume(self):
        pi = math.pi
        vCm = pi * (self.raio ** 2) * self.altura

        if self.unidade == "cm":
            return vCm / 1000
        else:
            return vCm

    def dicionario(self):
        """Converte o objeto para um dicionário para salvar como JSON."""
        return {
            "nome": self.nome,
            "unidade": self.unidade,
            "altura": self.altura,
            "raio": self.raio,
            "volume": self.volume()
        }





# Array de cilindros
try:
    objetos = [
        Cilindro("Xícara-azul", "cm", 7, 4),
        Cilindro("Garrafinha", "cm", 19, 3)
    ]
except ValueError as e:
    print(f"Erro ao criar cilindro: {e}")






# Salvando os objetos em um arquivo .txt (formato JSON)
with open("cilindros.txt", "w", encoding="utf-8") as arquivo:
    json.dump([obj.dicionario() for obj in objetos], arquivo, indent=4, ensure_ascii=False)

# Lendo os objetos do arquivo .txt
with open("cilindros.txt", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

# Loop exibindo cada cilindro contido no cilindros.txt
print("\n###############")
for cilindro in dados:
    print(f"{cilindro['nome']}, volume em litros: {cilindro['volume']}")
print("###############\n")


