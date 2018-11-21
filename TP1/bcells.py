from Tkinter import *
import PIL
from PIL import ImageTk, Image


class bCell(object):
	
	def __init__(self):
		self.bCell = ImageTk.PhotoImage(Image.open("##.png"))
		self.bCellSize = self.bCell.size
		self.cX = cx # TBD
		self.cY = cx # TBD
		self.speed = 10


	def collidesWithAntigen(self):
		# produces plasma cell that produces antibodies



class bPlasmaCell(bCell):

	def __init__(self):
		self.bPlasmaCell = ImageTk.PhotoImage(Image.open("##.png"))


class bMemoryCell(bCell):
# gets stored on side box once b cell is activated

	def __init__(self):
		self.bMemoryCell = ImageTk.PhotoImage(Image.open("##.png"))
