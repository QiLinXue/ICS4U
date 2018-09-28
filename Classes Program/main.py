#-----------------------------------------------------------------------------
# Name:        Chess Simulator
# Purpose:     To simulate Chess Positions
#
# Author:      QiLin
# Created:     18-Sep-2018
# Updated:     28-Sep-2018
#-----------------------------------------------------------------------------

# Import Start
from __init__ import *
from functions import *
from piece  import *
from chessboard import *

# Create Screen
wn = turtle.Screen()
wn.listen()

# Turtle Setup
turtle.tracer(0, 0)
pen.speed(0)
pen.ht()

# Main Program

#Initialize Classes
mainBoard = ChessBoard()
mainBoard.display()
wn.update()

# Always Runs
while True:
  wn.onclick(mainBoard.selectPiece)  

  
