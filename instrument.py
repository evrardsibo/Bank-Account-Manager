class Instrument :
    instrument = ""

    def __init__(self , musician) :
        self.musician = musician

    def play(self) :
        print( f"{self.musician} est en train de jouer avec l'instrument {self.instrument}" )

    def stop(self) :
        print( f"{self.instrument} a arrete de jour" )
