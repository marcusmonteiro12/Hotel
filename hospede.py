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

    def resumo (self):
        print ("Nome: " + self.nome.title())
        print ("Quarto: " + str (self.quarto))
        print ("Estrelas: " + str (self.estrelas))
        print ("Tempo de estadia: " + str (self.tempo_estadia) + " dias")
        print ("Total: " + 'R$' + str (self.preco_total()) + ',00')

    def preco_total (self): 
        if self.estrelas == 1: return 15 * int (self.tempo_estadia)
        elif self.estrelas == 2: return 30 * int (self.tempo_estadia)
        elif self.estrelas == 3: return 50 * int (self.tempo_estadia)