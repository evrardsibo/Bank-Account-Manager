import random


class Hero :
    lvl = 1

    def __init__(self , name) :
        self.name = name
        self.hp = 5

    def find_ennemy(self , ennemy) :

        if ennemy.lvl <= self.lvl :
            self.lvl += 1
            print( "Vous avez gagné ! Vous êtes maintenant au niveau" , self.lvl )
        else :
            print( "Vous avez perdu contre un ennemi de niveau" , ennemy.lvl )
            self.hp -= 1
            if self.hp == 0 :
                print( "Vous êtes mort au niveau" , self.lvl )
            else :
                print( "Il vous reste" , self.hp , "points de vie" )


class Ennemy( Hero ) :
    lvl = random.randrange( Hero.lvl - 1 , Hero.lvl + 2 )
    # lvl = random.randint(Hero.lvl - 1,Hero.lvl + 1)
    # lvl = Hero.lvl + random.choices([-1,0,1])


hero_name = 'Guy Banvil'
hero = Hero( hero_name )
print( f'Hello {hero.name} bienvenue, tu as {hero.hp} point de vie et tu commences au niveau {hero.lvl}' )

ennemy = Ennemy( 'ennemy' )
print( ennemy.name + "    " + str( ennemy.lvl ) )
while True:
    hero.find_ennemy( ennemy )
    if hero.hp <= 0 :
        print( "Vous avez perdu !" )
