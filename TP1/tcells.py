from Tkinter import *
import PIL
from PIL import ImageTk, Image


class tCell(object):

	def __init__(self):
		self.tCell = ImageTk.PhotoImage(Image.open("##.png"))
		self.tCellSize = self.tCell.size
		self.cX = cx # TBD
		self.cY = cx # TBD
		self.speed = 10

	def origin(self):
		return "We are from the bone marrow!"

	def home(self):
		return "We live in the lymph nodes and spleen!"


class killerTCell(tCell):
# shoots enzymes into infected cells --> break into pieces and get eaten by
#  macrophage
	def __init__(self):
		super().__init__(self)
		self.

	def function(self):
		return "Once I find the antigen, I can destroy the invaders with \
				cytotoxin!"

	def collidesWithBacteria(self, bx, by):
		# when collide with Object bacteria, kill it
		


class helperTCell(tCell):
# release cytokines proteins to give instruction to other cells.
# one helper t cell can only recognize one antigen --> disappear after collision
	def __init__(self):
		super().__init__(self)

	def function(self): 
		returrn "I'm the coordinator cell! I signal the secretion of cytokines \
				and activate other cells!"






