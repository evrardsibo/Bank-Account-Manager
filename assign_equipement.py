
import datetime

# Dictionnaire pour stocker les heures d'arrivée et de départ
pointages = {}

# Fonction pour enregistrer l'heure d'arrivée
def enregistrer_arrivee(nom):
    heure_arrivee = datetime.datetime.now()
    if nom in pointages:
        pointages[nom]['arrivees'].append(heure_arrivee)
    else:
        pointages[nom] = {'arrivees': [heure_arrivee], 'departs': []}
    print(f"{nom} est arrivé(e) à {heure_arrivee}")

# Fonction pour enregistrer l'heure de départ
def enregistrer_depart(nom):
    heure_depart = datetime.datetime.now()
    if nom in pointages:
        pointages[nom]['departs'].append(heure_depart)
        print(f"{nom} est parti(e) à {heure_depart}")
    else:
        print(f"{nom} n'a pas d'heure d'arrivée enregistrée.")

# Exemple d'utilisation
enregistrer_arrivee("Alice")
enregistrer_depart("Alice")

# Afficher les pointages
for nom, heures in pointages.items():
    print(f"{nom} :")
    for arrivee, depart in zip(heures['arrivees'], heures['departs']):
        print(f"  Arrivée : {arrivee}, Départ : {depart}")
