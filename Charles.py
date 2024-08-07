
from random import choice

class Charles:

    def __init__(self):
        pass

    def habiller_charles(self):
        vetements = []
        vetements.append(
            str(input("Charles porte un chandail de quelle couleur ?\n"))
        )
        vetements.append(
            str(input("Charles porte un pantalon de quelle couleur ?\n"))
        )
        return vetements


    def frapper_Charles(self, x):
        print(f"\nNous allons maintenant faire mal à Charles !")
        douleur =["aie", "ayoye", "hey colis", "OUCH"]
        for i in range(int(x)):
            print(f'{choice(douleur)}\n')
        print("Charles à vraiment mal maintenant !")

