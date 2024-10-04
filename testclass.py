from datetime import datetime


class Banque:
    def __init__(self, nom):
        self.nom = nom
        self.clients = []

    def ajouter_client(self, client):
        self.clients.append(client)

class Client:
    def __init__(self, nom, prenom, age, banque):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.banque = banque
        self.comptes = []

    def ouvrir_compte(self, compte):
        self.comptes.append(compte)

    def fermer_compte(self, compte):
        self.comptes.remove(compte)

class Compte:
    def __init__(self, proprietaire, solde=0):
        self.proprietaire = proprietaire
        self.solde = solde
        self.date_ouverture = datetime.now()

    def deposer(self, montant):
        self.solde += montant

    def retirer(self, montant):
        if montant <= self.solde:
            self.solde -= montant
        else:
            print("Fonds insuffisants")

    def afficher_solde(self):
        print(f"Solde: {self.solde}€")

class CompteCourant(Compte):
    pass

class CompteEpargne(Compte):
    def __init__(self, proprietaire, solde=0, taux_interet=0.01):
        super().__init__(proprietaire, solde)
        self.taux_interet = taux_interet

    def percevoir_interets(self):
        self.solde += self.solde * self.taux_interet

    def prime_anniversaire(self):
        if datetime.now().date() == self.date_ouverture.date():
            print(datetime.now().date())
            self.solde += 0.50

def virement(compte_source, compte_dest, montant):
    if compte_source.solde >= montant:
        compte_source.retirer(montant)
        compte_dest.deposer(montant)
    else:
        print("Fonds insuffisants pour le virement")

# Exemple d'utilisation
banque = Banque("MaBanque")
client1 = Client("Dupont", "Jean", 30, banque)
client2 = Client("Martin", "Alice", 28, banque)

compte1 = CompteCourant(client1, 1000)
compte2 = CompteEpargne(client1, 500)
compte3 = CompteCourant(client2, 1500)

client1.ouvrir_compte(compte1)
client1.ouvrir_compte(compte2)
client2.ouvrir_compte(compte3)

virement(compte1, compte3, 200)
compte2.percevoir_interets()
compte2.prime_anniversaire()

compte1.afficher_solde()
compte2.afficher_solde()
compte3.afficher_solde()
