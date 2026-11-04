
class Animal:
    def parler(self):
        raise NotImplementedError("Cette méthode doit être implémentée par les sous-classes.")


class Chien(Animal):
    def parler(self):
        return "Ouaf !"


class Chat(Animal):
    def parler(self):
        return "Miaou !"

class Vache(Animal):
    def parler(self):
        return "Meuh !"

class Robot:
    def parler(self):
        return "Bip Bip !"


def faire_parler(objet):
    print(objet.parler())


if __name__ == "__main__":
    print("Test Polymorphisme")
    
    animaux = [Chien(), Chat(), Vache(), Chien()]
    
    print("\nTOUS LES ANIMAUX PARLENT :")
    for a in animaux:
        faire_parler(a)
        
    print("\nTest du Duck Typing")
    mon_robot = Robot()
    faire_parler(mon_robot)