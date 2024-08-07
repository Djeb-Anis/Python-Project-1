

from Etudiant import Etudiant

from Personne import Personne


p1 = Personne("a", "b")
print(p1.__string__)

p2 = Etudiant("q", "w", 123456)
p3 = Employe("u", "w", 90)

l = []
l.append(p1)
l.append(p2)
l.append(p3)

for x in l :
    print(x,__str__())