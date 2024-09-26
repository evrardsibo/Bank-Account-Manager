from instrument import Instrument


class Batterie( Instrument ) :
    instrument = "baterrie"

    def __init__(self , musician) :
        super( ).__init__( musician )
