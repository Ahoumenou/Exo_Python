class Contact:
    def __init__(self, nom, prenom, telephone, email):
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.email = email

    def __str__(self):
        return f"Nom: {self.nom}, Prénom: {self.prenom}, Téléphone: {self.telephone}, Email: {self.email}"
