from __init__ import *
from functions import *

# Chess Piece
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
		
		Returns
		-------
		none
			
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
    return
  
