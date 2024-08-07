# Class Personne

class Personne:
    def __init__(self, p_nom, p_prenom):
    self.nom = p_nom
    self.prenom = p_prenom

    def __str__(self):
        return self.nom + "" + self.prenom