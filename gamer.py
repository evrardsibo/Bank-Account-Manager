import string


class Player :
    def __init__(self , name) :
        self.name = name
        self.grid = Grid( )
        self.grid_shoot = Grid( )
        self.ships = [ ]
        self.is_winner = False

    def ask_cordinates(self) :
        cordinatres = input( f"{self.name}" )
        column = int( string.ascii_uppercase.index( cordinatres[ 0 ] ) )
        row = int( cordinatres[ 1 : ] )
        return row , column

    def add_boat_to_grid(self) :
        while len( self.ships ) :
            column , row = self.ask_cordinates( )
            size = int( input( "Taille du boat 2 or 5 ?" ) )
            orientation = input( "Vertical ou horizontal ?" )
            boat = Ship( size , orientation , row , column )
            self.ships.append( boat )
        self.grid.update_board( self.ships )
        self.grid.display( )

    def shoot_grid(self) :
        column , row = self.ask_cordinates( )
        if prayer.grid.board[ row ][ column ] == "_" :
            print( "Null" )
            self.grid_shoot.board = "0"
        else :
            print( "Touche" )
            self.grid_shoot.board = "0"


class Ship :
    def __init__(self , size , orientation , location_row , location_col) :
        self.size = size
        self.location = [ ]
        self.orientation = orientation
        self.is_distroyed = False
        for case in range( self.size ) :
            if self.orientation == "vertical" :
                self.location.append( [ location_row + case , location_col ] )
            elif self.orientation == "horizontal" :
                self.location.append( [ location_row , location_col + case ] )
            else :
                print( "Invalid orientation" )
                break


class Grid :
    row = 10
    col = 10

    def __init__(self) :
        self.board = [ ]
        self.col_name = ""
        for number in range( self.col ) :
            self.col_name += string.ascii_uppercase[ number ]
            self.board = [ [ "_" ] * self.col for _ in range( self.row ) ]

    def display(self) :
        print( "\n" + " ".join( self.col_name[ col ] for col in range( self.col ) ) )
        for row in range( self.row ) :
            print( str( row ) + " " + " ".join( str( board ) for board in self.board[ row ] ) )

    def update_board(self , ship_list) :
        for ship in ship_list :
            for case in ship.location :
                self.board[ case[ 0 ] ][ case[ 1 ] ] = "S"


prayer = Player( "Jojo" )
prayer.add_boat_to_grid( )


class Game :
    pass
