'''
Classes which are responsible for holding the information
for each piece and their arrangements
'''

# Import Statements
from __init__ import *
from functions import *

# ---------------------
# --- Classes Start ---
# ---------------------

# Piece Class
class Piece:

  '''
  A piece object that describes each individual piece

  Attributes
  ----------
  color: str
    Contains the color (white / black)
  name: str
    Determines the symbol (pawn / rook / knight / bishop / queen / king)
  x : int
    Determines the x position x -> [0,7]
  y : int
    Determines the y position y -> [0,7]
  alive : bool
    Determines whether or not the screen shows the piece

  Methods
  -------
  printStats() -> None
    Prints out info to console

  '''
  
  def __init__(self,color,name,x,y,alive=True):
    '''

		Constructor to build a piece object

    Parameters
    ----------
    color: str
      Contains the color (white / black)
      If error, it sets it to white
    name: str
      Determines the symbol (pawn / rook / knight / bishop / queen / king)
      If error, it sets it to pawn
    x : int
      Determines the x position x -> [0,7]
      If error, it sets it to random
    y : int
      Determines the y position y -> [0,7]
      If error, it sets it to random
    alive : bool
      Determines whether or not the screen shows the piece
      If error or if default, it sets it to True
			
		..note:: that the "self" parameter is not listed in this section.
			
			
		'''

    # Set Color
    if color == "black" or color == "white": self.color = color
    else: color = "white"

    # Determine symbol based off of color and name
    if color == "black":
      if name == "pawn": self.name = u'♟'
      elif name == "rook": self.name = u'♜'
      elif name == "knight": self.name = u'♞'
      elif name == "bishop": self.name = u'♝'
      elif name == "queen": self.name = u'♛'
      elif name == "king": self.name = u'♚'
      else: self.name = u'♟'
    elif color == "white":
      if name == "pawn": self.name = u'♙'
      elif name == "rook": self.name = u'♖'
      elif name == "knight": self.name = u'♘'
      elif name == "bishop": self.name = u'♗'
      elif name == "queen": self.name = u'♕'
      elif name == "king": self.name = u'♔'
      else: self.name = u'♙'
    
    # Position
    if x < 8 and x > -1: self.x = x
    else: self.x = randint(0,7)

    if y < 8 and y > -1: self.y = y
    else: self.y = randint(0,7)

    # Alive or Not
    if alive or not alive: self.alive = alive
    else: self.alive = True
  
  def printStats(self):
    '''

    Prints out name, x pos, y pos, and color
      
    Parameters
    ----------
    none

    Returns
    -------
    none

    '''
    print(self.name, self.x + 1, self.y + 1, self.color)
    return True
  
# Chess Board Class
class ChessBoard:
  '''
  A book object that hold the pieces and their location on the board

  Attributes
  ----------
  pieces: object Array (Piece)
    Contains a list of all piece objects
    Defaults to a regular board setup (FIDE Regulations)
  
  Methods
  -------
  display() -> None
    Displays the board to the window

  selectPiece(x : float, y : float) -> None
    Prints the Stats of a piece based off of x and y coordinates
  
  '''

  global size

  def __init__(self,
    pieces = [
               Piece("black","pawn",0,6), Piece("black","rook",0,7),
               Piece("black","pawn",1,6), Piece("black","knight",1,7),
               Piece("black","pawn",2,6), Piece("black","bishop",2,7),
               Piece("black","pawn",3,6), Piece("black","queen",3,7),
               Piece("black","pawn",4,6), Piece("black","king",4,7),
               Piece("black","pawn",5,6), Piece("black","bishop",5,7),
               Piece("black","pawn",6,6), Piece("black","knight",6,7),
               Piece("black","pawn",7,6), Piece("black","rook",7,7),

               Piece("white","pawn",0,1), Piece("white","rook",0,0),
               Piece("white","pawn",1,1), Piece("white","knight",1,0),
               Piece("white","pawn",2,1), Piece("white","bishop",2,0),
               Piece("white","pawn",3,1), Piece("white","queen",3,0),
               Piece("white","pawn",4,1), Piece("white","king",4,0),
               Piece("white","pawn",5,1), Piece("white","bishop",5,0),
               Piece("white","pawn",6,1), Piece("white","knight",6,0),
               Piece("white","pawn",7,1), Piece("white","rook",7,0),
              ]
    ):

    '''
		Constructor to build the chess board
		
		Parameters
		----------
    pieces: object Array (Piece)
      Contains a list of all piece objects

		..note:: that the "self" parameter is not listed in this section.

		'''

    self.pieces = pieces
  
  def display(self):
    '''		
		Displays the board as well as each piece
		
    Parameters
    ----------
    none

		Returns
		-------
		none
		
		'''

    for piece in self.pieces:
      if piece.alive:
        ellipse(piece.x*size-4*size,piece.y*size-4*size,size)
        text(piece.name,piece.x*size-4*size+0.5*size,piece.y*size-4*size+0.5*size)

    for x in range(8):
      for y in range(8):
        rect(x*size-4*size,y*size-4*size,size,size)

    return
  
  def selectPiece(self, x, y):
    '''
    Converts window coordinates to board coordinates and prints stats for that coordinate

    Parameters
    ----------
    x : float
      The x position of the mouse
    y : float
      The y position of the mouse

    Returns
    -------
    none

    '''
    x = math.floor((4*size+x)/size)
    y = math.floor((4*size+y)/size)

    for piece in self.pieces:
      if piece.alive and piece.x == x and piece.y == y:
        piece.printStats()
