from instrument import Instrument


class Piano( Instrument ) :
    instrument = "piano"

    def __init__(self , musician) :
        super( ).__init__( musician )
