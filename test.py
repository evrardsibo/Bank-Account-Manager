class Orchestre:
    def __init__(self):
        self.instruments = []

    def ajouter_instrument(self, instrument):
        self.instruments.append(instrument)

    def concerto(self):
        for instrument in self.instruments:
            instrument.jouer()

class Instrument:
    def __init__(self, nom):
        self.nom = nom

    def jouer(self):
        print(f"{self.nom} joue sa mélodie.")

# Exemple d'utilisation
orchestre = Orchestre()
violon = Instrument("Violon")
piano = Instrument("Piano")
flute = Instrument("Flûte")

orchestre.ajouter_instrument(violon)
orchestre.ajouter_instrument(piano)
orchestre.ajouter_instrument(flute)

orchestre.concerto()
