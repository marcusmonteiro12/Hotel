from hospede import Hospede

while True:
    nome = input ("Informe o nome\n")
    quarto = int (input ("Informe o número do quarto\n"))
    estrelas = int (input ("Informe o número de estrelas do quarto\n"))
    tempo_estadia = int (input ("Informe o tempod de estadia em dias\n"))

    cliente = Hospede (nome, quarto, estrelas, tempo_estadia)
    break

print (cliente.nome)
