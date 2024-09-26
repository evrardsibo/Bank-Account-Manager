from instrument import Instrument


class Guitare( Instrument ) :
    instrument = "guitare"

    def __init__(self , musician) :
        super( ).__init__( musician )
