from __init__ import *
from functions import *
from piece import *

# Chess Board
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

    Returns
    -------
    none
    
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
