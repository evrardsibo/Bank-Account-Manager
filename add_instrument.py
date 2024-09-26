class Orchestre:

    def __init__(self,):
        self.instruments = [ ]

    def add_instrument(self,instrument):
        self.instruments.append(instrument)

    def concertos(self):
        for i in self.instruments:
            i.play()

