from banques import Banks
from customers import Coustomrs

bank1 = Banks( "ING" )
coustome = Coustomrs( "Evrard" , "sibo" , 40 , bank1 )
coustome.create_account(5000)
coustome.create_account(8000)
print(coustome.count)
print(f"{coustome.first_name} {coustome.last_name} {coustome.age} {coustome.bank.name} {coustome.balence()}")