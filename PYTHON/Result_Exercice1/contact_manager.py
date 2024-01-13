from contact import Contact

class ContactManager:
    def __init__(self):
        self.contacts = []

    def ajouter_contact(self, contact):
        self.contacts.append(contact)
        print("Contact ajouté avec succès!")

    def afficher_contacts(self):
        if not self.contacts:
            print("Aucun contact trouvé.")
        else:
            for contact in self.contacts:
                print(contact)

    def mettre_a_jour_contact(self, nom, prenom, nouveau_telephone, nouveau_email):
        contact_trouve = False
        for contact in self.contacts:
            if contact.nom == nom and contact.prenom == prenom:
                contact.telephone = nouveau_telephone
                contact.email = nouveau_email
                contact_trouve = True
                print("Contact mis à jour avec succès!")
                break

        if not contact_trouve:
            print("Contact non trouvé.")

    def supprimer_contact(self, nom, prenom):
        self.contacts = [contact for contact in self.contacts if not (contact.nom == nom and contact.prenom == prenom)]
        print("Contact supprimé avec succès!")

# Programme principal
if __name__ == "__main__":
    contact_manager = ContactManager()

    while True:
        print("\nMenu:")
        print("1. Ajouter un nouveau contact")
        print("2. Afficher tous les contacts")
        print("3. Mettre à jour un contact")
        print("4. Supprimer un contact")
        print("5. Quitter l'application")

        choix = input("Choisissez une option (1-5): ")

        if choix == "1":
            nom = input("Nom: ")
            prenom = input("Prénom: ")
            telephone = input("Téléphone: ")
            email = input("Email: ")
            nouveau_contact = Contact(nom, prenom, telephone, email)
            contact_manager.ajouter_contact(nouveau_contact)

        elif choix == "2":
            print("\nListe des contacts:")
            contact_manager.afficher_contacts()

        elif choix == "3":
            nom = input("Nom du contact à mettre à jour: ")
            prenom = input("Prénom du contact à mettre à jour: ")
            nouveau_telephone = input("Nouveau téléphone: ")
            nouveau_email = input("Nouvel email: ")
            contact_manager.mettre_a_jour_contact(nom, prenom, nouveau_telephone, nouveau_email)

        elif choix == "4":
            nom = input("Nom du contact à supprimer: ")
            prenom = input("Prénom du contact à supprimer: ")
            contact_manager.supprimer_contact(nom, prenom)

        elif choix == "5":
            print("Merci d'avoir utilisé le gestionnaire de contacts. Au revoir!")
            break

        else:
            print("Option invalide. Veuillez choisir une option valide.")
