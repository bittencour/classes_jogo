class heroiAventura:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def ataqueHeroi(self):
        if self.tipo == "mago":
            return "Magia"
        elif self.tipo == "guerreiro":
            return "espada"
        elif self.tipo == "monge":
            return "artes marciais"
        else:
            return "espada"

nomeHeroi = input("Qual o nome do Herói? ")
idadeHeroi = int(input("Qual a idade do Herói? "))
tipoHeroi = input("Qual o tipo do Herói? ")

heroiAtaque = heroiAventura(nomeHeroi, idadeHeroi, tipoHeroi)

tipoAtaque = heroiAtaque.ataqueHeroi()
print("O " + tipoHeroi + " atacou usando " + str(tipoAtaque))

