from personagens import Elfo, Humano, Mago, Orc, Paladino, Personagem


#função para a batalha entre dois personagens
def batalha(personagem1: Personagem, personagem2: Personagem):
  print(f"{personagem1.nome} enfrentará {personagem2.nome}")

  while personagem1.esta_vivo() and personagem2.esta_vivo():
    personagem1.atacar(personagem2)
    if personagem2.esta_vivo():
      personagem2.atacar(personagem1)

    print("================== Inicio do round ==================")
    print(f"{personagem1.nome}: {personagem1.vida} HP")
    print(f"{personagem2.nome}: {personagem2.vida} HP")
    print("================== Fim do round ==================")

def batalha_tripla(personagem1: Personagem, personagem2: Personagem, personagem3: Personagem):
  print(f"{personagem1.nome} , {personagem2.nome} e {personagem3.nome} se enfrentarão")

  while personagem1.esta_vivo() or personagem2.esta_vivo() or personagem2.esta_vivo():
    personagem1.atacar(personagem2)
    if personagem2.esta_vivo():
      personagem2.atacar(personagem3)
      if personagem3.esta_vivo():
        personagem3.atacar(personagem1)

    print("================== Inicio do round ==================")
    print(f"{personagem1.nome}: {personagem1.vida} HP")
    print(f"{personagem2.nome}: {personagem2.vida} HP")
    print(f"{personagem3.nome}: {personagem3.vida} HP")
    print("================== Fim do round ==================")

#criar personagens
paladino1 = Paladino("Aragorn")
mago1 = Mago("Gandalf")
elfo1 = Elfo("Legolas")
humano1 = Humano("Frodo")
orc1 = Orc("Grom")

#batalhas
#batalha(paladino1, orc1)
#batalha(mago1, elfo1)
batalha_tripla(elfo1, humano1, paladino1)