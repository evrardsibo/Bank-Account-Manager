from add_instrument import Orchestre
from batterie import Batterie
from guitare import Guitare
from instrument import Instrument
from piano import Piano

instrument = Instrument( "evaken" )
guitare = Guitare( "eva" )
piono = Piano( "ken" )
batterie = Batterie("batterie")
batterie.stop()
orchestre = Orchestre()
orchestre.add_instrument(guitare)
orchestre.add_instrument(piono)
orchestre.add_instrument(batterie)
orchestre.concertos()




