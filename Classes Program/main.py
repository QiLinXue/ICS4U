#-----------------------------------------------------------------------------
# Name:        Chess Simulator
# Purpose:     To simulate Chess
#
# Author:      QiLin
# Created:     18-Sep-2018
# Updated:     26-Sep-2018
#-----------------------------------------------------------------------------

# Import Start
import turtle
import math

# Create Pen and Screen
pen = turtle.Turtle()
wn = turtle.Screen()

# Listens for Mouse Events
wn.listen()

# Turtle Setup
turtle.tracer(0, 0)
pen.speed(4)
pen.ht()

# Determines size of everything
size = 100

# Functions Start
def rect(x, y, length, width): 
  """
	Function to draw a rectangle

	Parameters
	----------
	x : int
		The x position of the bottom left corner

  y: int
    The y position of the bottom left corner

  length: int
    The horizontal distance

  width: int
    The vertical distance

  Returns
	-------
	none
  """
  pen.pu()
  pen.goto(x,y)
  pen.pd()
  pen.pensize(3)
  pen.forward(length)
  pen.left(90)
  pen.forward(width)
  pen.left(90)
  pen.forward(length)
  pen.left(90)
  pen.forward(width)
  pen.left(90)
def ellipse(x, y, diameter):
  """
	Function to draw a circle

	Parameters
	----------
	x : int
		The x position of the bottom left corner

  y: int
    The y position of the bottom left corner

  diameter: int
    The horizontal distance

  Returns
	-------
	none
  """
  pen.pu()
  pen.goto(x+diameter/2,y)
  pen.pd()
  pen.circle(diameter/2)
def text(arg, x, y):
  """
	Function to draw text

	Parameters
	----------
  arg : str
    The string which is displayed

	x : int
		The x position of the bottom left corner

  y: int
    The y position of the bottom left corner

  Returns
	-------
	none
  """
  pen.pu()
  pen.goto(x,y-20)
  pen.pd()
  pen.write(arg,False,"center",("Arial","40","normal"))

# Classes Start

# Chess Piece
class Piece:
  '''
  A book object that describes each individual piece
  '''
  
  def __init__(self,color,name,x,y,alive=True):

    # Determine symbol based off of color and name
    if color == "black":
      if name == "pawn": self.name = u'♟'
      elif name == "rook": self.name = u'♜'
      elif name == "knight": self.name = u'♞'
      elif name == "bishop": self.name = u'♝'
      elif name == "queen": self.name = u'♛'
      elif name == "king": self.name = u'♚'
    elif color == "white":
      if name == "pawn": self.name = u'♙'
      elif name == "rook": self.name = u'♖'
      elif name == "knight": self.name = u'♘'
      elif name == "bishop": self.name = u'♗'
      elif name == "queen": self.name = u'♕'
      elif name == "king": self.name = u'♔'
    
    # Position
    self.x = x
    self.y = y

    # Alive or Not
    self.alive = alive
  
  def die(self):
    self.alive = False
    print("died")
  

# Chess Board
class ChessBoard:
  '''
  A book object that hold the pieces and their location on the board

  Attributes
  ----------
  bPieces: 2D Array
    Stores the symbol (str), x pos (int), and y pos (int) for each individual black piece
  
  wPieces : 2D Array
    Stores the symbol (str), x pos (int), and y pos (int) for each individual white piece

  Methods
  -------
  display() -> None
    Displays the board to the window
  '''

  global size

  def __init__(self,
    # bPieces=[ [u'♜',0,7], 
    #           [u'♞',1,7], [u'♝',2,7], [u'♛',3,7], [u'♚',4,7], [u'♝',5,7], [u'♞',6,7], [u'♜',7,7],
    #           [u'♟',0,6], [u'♟',1,6], [u'♟',2,6], [u'♟',3,6], [u'♟',4,6], [u'♟',5,6], [u'♟',6,6], [u'♟',7,6]
    #         ],

    # wPieces=[ [u'♙',0,1], [u'♙',1,1], [u'♙',2,1], [u'♙',3,1], [u'♙',4,1], [u'♙',5,1], [u'♙',6,1], [u'♙',7,1],
    #           [u'♖',0,0], [u'♘',1,0], [u'♗',2,0], [u'♕',3,0], [u'♔',4,0], [u'♗',5,0], [u'♘',6,0], [u'♖',7,0]
    #         ]
    bPieces = [
               Piece("black","pawn",0,6), Piece("black","rook",0,7),
               Piece("black","pawn",1,6), Piece("black","knight",1,7),
               Piece("black","pawn",2,6), Piece("black","bishop",2,7),
               Piece("black","pawn",3,6), Piece("black","queen",3,7),
               Piece("black","pawn",4,6), Piece("black","king",4,7),
               Piece("black","pawn",5,6), Piece("black","bishop",5,7),
               Piece("black","pawn",6,6), Piece("black","knight",6,7),
               Piece("black","pawn",7,6), Piece("black","rook",7,7),
              ],
    wPieces = [
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
    self.wPieces = wPieces
    self.bPieces = bPieces
  
  def display(self):
    '''		
		Displays the board as well as each piece
		
		Returns
		-------
		none
		
		'''

    for piece in self.wPieces:
      ellipse(piece.x*size-4*size,piece.y*size-4*size,size)
      text(piece.name,piece.x*size-4*size+0.5*size,piece.y*size-4*size+0.5*size)

    for piece in self.bPieces:
      ellipse(piece.x*size-4*size,piece.y*size-4*size,size)
      text(piece.name,piece.x*size-4*size+0.5*size,piece.y*size-4*size+0.5*size)

    for x in range(8):
      for y in range(8):
        rect(x*size-4*size,y*size-4*size,size,size)

    return
  
  def selectPiece(self,x,y):
    x = math.floor((400+x)/100)
    y = math.floor((400+y)/100)
    self.wPieces[0].die()
    print(x,y)

# Main Program

#Initialize Classes
mainBoard = ChessBoard()
mainBoard.display()

while (True):
  wn.onclick(mainBoard.selectPiece)
  turtle.update()
