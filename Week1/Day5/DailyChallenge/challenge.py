import math


class Circle:
    """
    Classe représentant un cercle géométrique.
    
    Un cercle est défini par son rayon. Le diamètre est calculé automatiquement.
    """
    
    def __init__(self, radius):
        """
        Initialise un cercle avec un rayon donné.
        
        Args:
            radius (float): Le rayon du cercle. Doit être positif.
        
        Raises:
            ValueError: Si le rayon est négatif.
        """
        if radius < 0:
            raise ValueError("Le rayon doit être positif.")
        self._radius = float(radius)
    
    @property
    def radius(self):
        """Retourne le rayon du cercle."""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """Définit le rayon du cercle."""
        if value < 0:
            raise ValueError("Le rayon doit être positif.")
        self._radius = float(value)
    
    @property
    def diameter(self):
        """Retourne le diamètre du cercle (2 * rayon)."""
        return 2 * self._radius
    
    @diameter.setter
    def diameter(self, value):
        """Définit le diamètre du cercle et met à jour le rayon."""
        if value < 0:
            raise ValueError("Le diamètre doit être positif.")
        self._radius = float(value) / 2
    
    def area(self):
        """
        Calcule et retourne l'aire du cercle.
        
        Returns:
            float: L'aire du cercle (π * r²).
        """
        return math.pi * self._radius ** 2
    
    def __str__(self):
        """Retourne une représentation lisible du cercle."""
        return f"Circle(radius={self.radius:.2f}, diameter={self.diameter:.2f}, area={self.area():.2f})"
    
    def __repr__(self):
        """Retourne une représentation technique du cercle."""
        return f"Circle({self.radius})"
    
    def __add__(self, other):
        """
        Additionne deux cercles et retourne un nouveau cercle.
        
        Le rayon du nouveau cercle est la somme des deux rayons.
        
        Args:
            other (Circle): Un autre cercle.
        
        Returns:
            Circle: Un nouveau cercle avec pour rayon la somme des deux rayons.
        """
        if not isinstance(other, Circle):
            return NotImplemented
        return Circle(self.radius + other.radius)
    
    def __eq__(self, other):
        """
        Vérifie si deux cercles sont égaux (même rayon).
        
        Returns:
            bool: True si les rayons sont égaux, False sinon.
        """
        if not isinstance(other, Circle):
            return NotImplemented
        return math.isclose(self.radius, other.radius)
    
    def __lt__(self, other):
        """
        Vérifie si ce cercle est plus petit qu'un autre (rayon inférieur).
        
        Returns:
            bool: True si self.radius < other.radius, False sinon.
        """
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius < other.radius
    
    def __gt__(self, other):
        """
        Vérifie si ce cercle est plus grand qu'un autre (rayon supérieur).
        
        Returns:
            bool: True si self.radius > other.radius, False sinon.
        """
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius > other.radius
    
    def __le__(self, other):
        """
        Vérifie si ce cercle est plus petit ou égal à un autre.
        
        Returns:
            bool: True si self.radius <= other.radius, False sinon.
        """
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius <= other.radius
    
    def __ge__(self, other):
        """
        Vérifie si ce cercle est plus grand ou égal à un autre.
        
        Returns:
            bool: True si self.radius >= other.radius, False sinon.
        """
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius >= other.radius



if __name__ == "__main__":
    # Création de cercles
    c1 = Circle(2)
    c2 = Circle(3.5)
    c3 = Circle(1.5)
    
    # Affichage
    print(c1)
    print(c2)
    print(c3)
    
    # Aire
    
    print(f"Aire de c1: {c1.area():.2f}")
    print(f"Aire de c2: {c2.area():.2f}")
    
    # Addition
    
    c4 = c1 + c2
    print(f"c1 + c2 = {c4}")
    
    # Comparaisons avec booléens
    
    print(f"c1 > c3: {c1 > c3}")
    print(f"c1 == Circle(2): {c1 == Circle(2)}")
    print(f"c1 < c2: {c1 < c2}")
    
    # Tri d'une liste
    
    circles = [c2, c1, c3, c4]
    print(f"Avant tri: {[c.radius for c in circles]}")
    circles_sorted = sorted(circles)
    print(f"Après tri: {[c.radius for c in circles_sorted]}")
    
    # Utilisation du diamètre
    
    c5 = Circle(5)
    print(f"Cercle c5 avec rayon 5 a diamètre: {c5.diameter}")
    c5.diameter = 20
    print(f"Après avoir défini diamètre à 20, rayon = {c5.radius}")
