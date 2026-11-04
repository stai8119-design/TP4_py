
from abc import ABC, abstractmethod
import math

class Forme(ABC):
    @abstractmethod
    def aire(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} – aire : {self.aire():.2f}"


class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        """Calcule l'aire d'un cercle : pi * r^2"""
        return math.pi * (self.rayon ** 2)


class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        """Calcule l'aire d'un rectangle : largeur * hauteur"""
        return self.largeur * self.hauteur


class Triangle(Forme):
    def __init__(self, base, hauteur):
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        """Calcule l'aire d'un triangle : (base * hauteur) / 2"""
        return 0.5 * self.base * self.hauteur


if __name__ == "__main__":
    print("Test du Polymorphisme avec des Formes Géométriques")
    
    formes = [
        Cercle(5),
        Rectangle(3, 4),
        Triangle(7, 2)
    ]

    print("\nAffichage des aires :")
    for f in formes:
        print(f)