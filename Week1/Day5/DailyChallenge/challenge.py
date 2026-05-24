class Circle:
    def __init__(self, rayon, diametre):
        self.rayon = rayon
        self.diametre = diametre
    @property
    def rayon(self):
        return self._rayon

    @rayon.setter
    def rayon(self, value):
        self._rayon = value

    @property
    def diametre(self):
        return self._diametre

    @diametre.setter
    def diametre(self, value):
        self._diametre = value

    def calculer_aire(self):
        return 3.14 * self.rayon ** 2
    
    def __str__(self):
        return f"Le cercle a rayon: {self.rayon} et diamètre: {self.diametre}"
    
    def __add__(self, other_circle):
        new_rayon = self.rayon + other_circle.rayon
        new_diametre = self.diametre + other_circle.diametre
        return Circle(new_rayon, new_diametre)
    
    def __gt__(self, other):
        if self.calculer_aire() > other.calculer_aire():
            return f"Le cercle avec rayon {self.rayon} est plus grand que le cercle avec rayon {other.rayon}"
    
    def __eq__(self, other):
        if self.calculer_aire() == other.calculer_aire():
            return f"Le cercle avec rayon {self.rayon} est égal au cercle avec rayon {other.rayon}"
    
    def __lt__(self, *args):
        liste_cercles = []
        for cercle in args:
            liste_cercles.append(cercle)
        return sorted(liste_cercles, key=lambda c: c.calculer_aire())
    
c1 = Circle(5, 10)
c2 = Circle(3, 6)
c3 = c1 + c2
print(c1)
print(c2)
print(c3)
print(c1 > c2)
print(c1 == c2)
print(c1 < c2, c3)