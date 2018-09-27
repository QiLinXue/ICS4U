#-----------------------------------------------------------------------------
# Name:        Chess Simulator
# Purpose:     To Simulate Custom Chess Positions
#
# Author:      QiLin
# Created:     18-Sep-2018
# Updated:     27-Sep-2018
#-----------------------------------------------------------------------------

# Import Start
from __init__ import *
from functions import *
from classes import *

# ------------------------
# --- Turtle Env Setup ---
# ------------------------

# Create Screen
wn = turtle.Screen()
wn.listen()

# Turtle Setup
turtle.tracer(0, 0)
pen.speed(0)
pen.ht()

# ------------------------
# ----- Main Program -----
# ------------------------

#Initialize Classes
mainBoard = ChessBoard()
mainBoard.display()
wn.update()

while (True):
  wn.onclick(mainBoard.selectPiece)  

  