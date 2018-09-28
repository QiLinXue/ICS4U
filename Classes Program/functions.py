'''
Functions File which contains graphical functions that can
draw rectangles, circles, and display text similar to Processing
documentation
'''

from __init__ import *

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
  pen.pensize(round(size/33.33))
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
  pen.goto(x,y-(size/5))
  pen.pd()
  pen.write(arg,False,"center",("Arial",str(round(size/2.5)),"normal"))
