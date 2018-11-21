# Bacteria

from Tkinter import *
import PIL
from PIL import ImageTk, Image


class Bacteria(object):
	
	def __init__(self, cX, cY):
		self.bacterias = ImageTk.PhotoImage(Image.open("bacteria.png"))
		self.bacSize = data.self.bacterias.bacSize
		self.cX = cX # TBD
		self.cY = cY # TBD
		self.scroll = 10

	# View

	def draw(self, canvas):
		canvas.create_image(data.cX, cY, image=data.bacterias)

	# Controller

	def collidesWithTCell(self):
		# once collide with macrophage, gets trapped --> eaten
		# once collide with Killer T cell --> shoots cytotoxin into 
		#  infected cells --> break into smaller pieces --> macrophage eat
		pass

	def reactToDying(self):
		# turn the color to gray and disappear in two sec
		pass



