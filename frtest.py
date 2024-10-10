class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

class Friterie:
    def __init__(self):
        self.stock = {}

    def ajouter_produit(self, produit, quantite):
        if produit.nom in self.stock:
            self.stock[produit.nom]['quantite'] += quantite
        else:
            self.stock[produit.nom] = {'produit': produit, 'quantite': quantite}

    def retirer_produit(self, nom_produit, quantite):
        if nom_produit in self.stock and self.stock[nom_produit]['quantite'] >= quantite:
            self.stock[nom_produit]['quantite'] -= quantite
            if self.stock[nom_produit]['quantite'] == 0:
                del self.stock[nom_produit]
        else:
            print("Quantité insuffisante ou produit non disponible.")

    def prendre_commande(self, commande):
        total = 0
        for nom_produit, quantite in commande.items():
            if nom_produit in self.stock and self.stock[nom_produit]['quantite'] >= quantite:
                total += self.stock[nom_produit]['produit'].prix * quantite
            else:
                print(f"Produit {nom_produit} non disponible ou quantité insuffisante.")
                return None
        for nom_produit, quantite in commande.items():
            self.retirer_produit(nom_produit, quantite)
        return total

# Exemple d'utilisation
friterie = Friterie()
frites = Produit("Frites", 2.5)
sauce = Produit("Sauce", 0.5)

friterie.ajouter_produit(frites, 10)
friterie.ajouter_produit(sauce, 20)

commande = {"Frites": 2, "Sauce": 3}
total = friterie.prendre_commande(commande)
if total is not None:
    print(f"Le total de la commande est de {total} euros.")
