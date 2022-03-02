# "estrelas" representa o nível do quarto
# 1 estrela: modesto (R$15,00/dia)
# 2 estrelas: razoável (R$30,00/dia)
# 3 estrelas: luxo (R$50,00/dia)

class Hospede ():
    def __init__(self, nome, quarto, estrelas, tempo_estadia):
        self.nome = nome
        self.quarto = quarto 
        self.estrelas = estrelas
        self.tempo_estadia = tempo_estadia

    def preco_total (self): 
        if self.estrelas == 1: return 15 * int (self.tempo_estadia)
        if self.estrelas == 2: return 30 * int (self.tempo_estadia)
        if self.estrelas == 3: return 50 * int (self.tempo_estadia)