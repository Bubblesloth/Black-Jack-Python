# Créé par pauvers, le 18/10/2022 en Python 3.7

class Pile:
    def __init__(self):
        self.pile = []

    def depiler(self):
        return self.pile.pop()

    def empiler(self, elmt):
        self.pile.append(elmt)

    def est_vide(self):
        return len(self.pile) == 0

def afficher(p):
    temp = Pile()
    while not p.est_vide():
        elt=p.depiler()
        print("|"+str(elt)+"|")
        temp.empiler(elt)
    while not temp.est_vide():
        p.empiler(temp.depiler())




p = Pile()
p.empiler(1)
p.empiler(2)
p.empiler(3)
afficher(p)


