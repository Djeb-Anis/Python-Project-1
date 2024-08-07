
from Personne import Personne
# Heritage

class Employe:
    def __init__(self, p_nom, p_prenom, p_num):
        Personne.__init__(self, p_nom, p_prenom)
        #super().__init__(self, p_nom, p_prenom)
        self.num = self.num

    def __str__(self):
        return super.__str__() + "" + str(self.num)
        #return self.nom + "" + self.prenom + self.num