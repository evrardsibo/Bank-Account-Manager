from add_instrument import Orchestre
from batterie import Batterie
from doctor import Doctor
from employ import Employ
from guitare import Guitare
from nurse import Nurse
from patient import Patient
from instrument import Instrument
from piano import Piano

# instrument = Instrument( "evaken" )
# guitare = Guitare( "eva" )
# piono = Piano( "ken" )
# batterie = Batterie("batterie")
# batterie.stop()
# orchestre = Orchestre()
# orchestre.add_instrument(guitare)
# orchestre.add_instrument(piono)
# orchestre.add_instrument(batterie)
# orchestre.concertos()

employ = Employ("amaki","turiho",29, "rohero",3000,"HR")
doctor = Doctor("amaki","turiho",39, "rohero",5000,"medicine generale","cardiologue")
nurse = Nurse("amaki","turiho",19, "rohero",2000,"nurse","pediatrie")
patient = Patient("amaki","turiho",9, "rohero")



patient.display_patient()
employ.display_employ()
nurse.display_nurse()
doctor.dispay_doctor()
