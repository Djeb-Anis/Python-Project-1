
from Personne import Personne
# Heritage

class Etudiant:
    def __init__(self, p_nom, p_prenom, p_DA):
        Personne.__init__(self, p_nom, p_prenom)
        # super().__init__(self, p_nom, p_prenom)
        self.DA = p_DA

    def __str__(self):
        return super().__str__() + "" str(self.DA)
        # return self.nom + "" + self.prenom + self.DA