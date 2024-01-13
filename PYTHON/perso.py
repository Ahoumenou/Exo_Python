class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

class GestionPersonnes:
    def __init__(self):
        self.personnes = []

    def ajouter_personne(self, personne):
        self.personnes.append(personne)

    def lire_personnes(self):
        return self.personnes

    def lire_personne_par_nom(self, nom):
        for personne in self.personnes:
            if personne.nom == nom:
                return personne
        return None

    def mettre_a_jour_personne(self, nom, nouvel_age):
        personne = self.lire_personne_par_nom(nom)
        if personne:
            personne.age = nouvel_age
            return True
        return False

    def supprimer_personne(self, nom):
        personne = self.lire_personne_par_nom(nom)
        if personne:
            self.personnes.remove(personne)
            return True
        return False

# Exemple d'utilisation
gestion_personnes = GestionPersonnes()

# Création et ajout de personnes
personne1 = Personne("Alice", 25)
personne2 = Personne("Bob", 30)
gestion_personnes.ajouter_personne(personne1)
gestion_personnes.ajouter_personne(personne2)

# Lecture de toutes les personnes
toutes_les_personnes = gestion_personnes.lire_personnes()
print("Toutes les personnes:", toutes_les_personnes)

# Lecture d'une personne par nom
personne_bob = gestion_personnes.lire_personne_par_nom("Bob")
print("Personne par nom:", personne_bob.__dict__)

# Mise à jour de l'âge de Bob
gestion_personnes.mettre_a_jour_personne("Bob", 32)
print("Personne mise à jour:", personne_bob.__dict__)

# Suppression d'une personne
gestion_personnes.supprimer_personne("Alice")
toutes_les_personnes_apres_suppression = gestion_personnes.lire_personnes()
print("Toutes les personnes après suppression:", toutes_les_personnes_apres_suppression)
