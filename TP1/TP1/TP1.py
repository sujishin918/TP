#################################################################
# Term Project
# Your Name: Suji Shin
# Your Andrew ID: sujis
# Your Section: O
#################################################################

from tkinter import *
import PIL
from PIL import ImageTk, Image
import math, random


# NOTES for TP1!
#
# I focused more on creating a general framework, instead of working on 
# a specific part of the code. As for class functions, I am considering 
# separating classes of cells into separate files. 
# 
# Then I have a animation part, which I divided into five modes, including
# starting and ending screens.
# 
# Many classes have "ImageTk.PhotoImage(Image.open("##.png"))" in init function.
# I will be replacing ##.png with actual images once I obtain them.




#######################
#   Class Functions	  #
#######################

## Class Bacteria ##

class Bacteria(object):

	def __init__(self):
		self.bac = ImageTk.PhotoImage(Image.open("##.png"))
		self.bacSize = self.bac.size
		self.initNum = 30


## Class Phagocytes ##

class Phagocytes(object):

	def __init__(self):
		self.phag = ImageTk.PhotoImage(Image.open("##.png"))
		self.phagSize = self.phag.size

	def presentAntigen(self):
		pass

	def activateAI(self):
		pass

	def killBacteria(self):
		pass 

class Macrophage(Phagocytes):
	def __init__(self):
		self.mac = ImageTk.PhotoImage(Image.open("##.png"))
		self.macSize = self.mac.size
		self.presentAntigen = False

class dendriticCell(Phagocytes):
	def __init__(self):
		self.dc = ImageTk.PhotoImage(Image.open("##.png"))
		self.dcSize = self.dc.size

	def activateAdaptive(self):
		# if engulfs macrophage:
		self.presentAntigen = True


## T-Cells ##

class tCell(object):

	def __init__(self):
		self.tCell = ImageTk.PhotoImage(Image.open("##.png"))
		self.tCellSize = self.tCell.size
		self.cX = cx # TBD
		self.cY = cx # TBD
		self.speed = 10
		self.location = "Lymph Node"

	def origin(self):
		return "We are from the bone marrow!"

	def home(self):
		return "We live in the lymph nodes!"

class killerTCell(tCell):
# shoots enzymes into infected cells --> break into pieces and get eaten by
#  macrophage
	def __init__(self):
		super().__init__(self)
		self.recognizeAntigen = False
		self.location = "Lymph Node"
		self.kt_cX = cx # TBD
		self.kt_cY = cx # TBD
		self.kt_r = 10 # must change later

	def function(self):
		return "Once I find the antigen, I can destroy the invaders with \
				cytotoxin!"

	def moveOut(self):
		self.location = "Infection Site"

	def collidesWithBacteria(self, bx, by, br):
		# when collide with Object bacteria, kill it
		radii = self.kt_r + br
		dist = math.sqrt((self.kt_cx-bx) ** 2 + (self.kt_cy - by) ** 2)
		if dist <= radii:
			return True
		# If true, remove from list in animation framework

	def recognizeAntigen(self):
		# recognize antigen present on bacteria
		pass

	def secretePerforin(self):
		# enzyme that breaks down bacterial membrane is secreted 
		# from Helper T cell
		pass

class helperTCell(tCell):
# release cytokines proteins to give instruction to other cells.
# one helper t cell can only recognize one antigen --> disappear after collision
	def __init__(self):
		super().__init__(self)
		self.bindToMacrophage = True
		self.location = "Lymph Node"

	def function(self): 
		returrn ("I signal the secretion of cytokines to activate other cells!")

	def activateBnKT(self):
		# secretes cytokines to activate B- & KT-cells
		pass


## B-Cells ##

class bCell(object):
	
	def __init__(self):
		self.bCell = ImageTk.PhotoImage(Image.open("##.png"))
		self.bCellSize = self.bCell.size
		self.location = "Lymph Node"

class bMemoryCell(bCell):

	def __init__(self):
		self.bPlasmaCell = ImageTk.PhotoImage(Image.open("##.png"))
		self.bPlasmaCell = self.bPlasmaCell.size
		self.location = "Lymph Node"

	def remain(self):
		# add memory cells to the corner box on the screen
		pass

class bPlasmaCell(bCell):

	def __init__(self):
		self.bPlasmaCell = ImageTk.PhotoImage(Image.open("##.png"))
		self.bPlasmaCell = self.bPlasmaCell.size
		self.antibody = ImageTk.PhotoImage(Image.open("##.png"))
		self.ig = []
		self.location = "Lymph Node"

	def moveOut(self):
		self.location = "Infection Site"

	def produceAntibody(self, canvas):
		cx = random.randint(20, 380)
		cy = random.randint(200, 380)
		self.ig.append((cx, cy))

	def antibodyKillBacteria(self):
		# When antibody comes in contact with bacteria, it destroys bac.
		pass


##############################################
# 				Animation  					 #    		
#											 #
# Animation Framework taken from 15-112 notes#
##############################################

## Initial Design ##

def init(data):
	data.mode = "startScreen"

## MODE DISPATCHER ##

def mousePressed(event, data):
	if data.mode == "startScreen":
		pass
	elif data.mode == "stage1":
		pass
	elif data.mode == "stage2":
		pass
	elif data.mode == "stage3":
		pass
	elif data.mode == "gameOver":
		pass

def keyPressed(event, data):
	if data.mode == "startScreen":
		pass
	elif data.mode == "stage1":
		pass
	elif data.mode == "stage2":
		pass
	elif data.mode == "stage3":
			pass
	elif data.mode == "gameOver":
		pass

def timerFired(data):
	if data.mode == "startScreen":
		pass
	elif data.mode == "stage1":
		pass
	elif data.mode == "stage2":
		pass
	elif data.mode == "stage3":
		pass
	elif data.mode == "gameOver":
		pass

def redrawAll(canvas, data):
	if data.mode == "startScreen":
		pass
	elif data.mode == "stage1":
		pass
	elif data.mode == "stage2":
		pass
	elif data.mode == "stage3":
		pass
	elif data.mode == "gameOver":
		pass


## STAGE 0 - START SCREEN ## 

def mousePressed_0(event, data):
	# use event.x and event.y
	pass

def keyPressed_0(event, data):
	# use event.char and event.keysym
	pass

def timerFired_0(data):
	pass

def redrawAll_0(canvas, data):
	# draw in canvas
	pass


## STAGE 1 - Innate / Infection Site ## 

def mousePressed_1(event, data):
	# use event.x and event.y
	pass

def keyPressed_1(event, data):
	# use event.char and event.keysym
	pass

def timerFired_1(data):
	pass

def redrawAll_1(canvas, data):
	# draw in canvas
	pass

## STAGE 2 - Adaptive / Lymph Node ##

def mousePressed_2(event, data):
	# use event.x and event.y
	pass

def keyPressed_2(event, data):
	# use event.char and event.keysym
	pass

def timerFired_2(data):
	pass

def redrawAll_2(canvas, data):
	# draw in canvas
	pass

## STAGE 3 - Adaptive / Infection Site ##

def mousePressed_3(event, data):
	# use event.x and event.y
	pass
	
def keyPressed_3(event, data):
	# use event.char and event.keysym
	pass
	
def timerFired_3(data):
	pass
	
def redrawAll_3(canvas, data):
	# draw in canvas
	pass

## STAGE 4 - End Screen ## 

def mousePressed_4(event, data):
	# use event.x and event.y
	pass

def keyPressed_4(event, data):
	# use event.char and event.keysym
	if event.keysym == "r":
		data.gameMode = "startScreen"

def timerFired_4(data):
	pass

def redrawAll_4(canvas, data):
	# draw in canvas
	pass

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
	def redrawAllWrapper(canvas, data):
		canvas.delete(ALL)
		canvas.create_rectangle(0, 0, data.width, data.height,
								fill='white', width=0)
		redrawAll(canvas, data)
		canvas.update()    

	def mousePressedWrapper(event, canvas, data):
		mousePressed(event, data)
		redrawAllWrapper(canvas, data)

	def keyPressedWrapper(event, canvas, data):
		keyPressed(event, data)
		redrawAllWrapper(canvas, data)

	def timerFiredWrapper(canvas, data):
		timerFired(data)
		redrawAllWrapper(canvas, data)
		# pause, then call timerFired again
		canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
	# Set up data and call init
	class Struct(object): pass
	data = Struct()
	data.width = width
	data.height = height
	data.timerDelay = 100 # milliseconds
	root = Tk()
	root.resizable(width=False, height=False) # prevents resizing window
	init(data)
	# create the root and the canvas
	canvas = Canvas(root, width=data.width, height=data.height)
	canvas.configure(bd=0, highlightthickness=0)
	canvas.pack()
	# set up events
	root.bind("<Button-1>", lambda event:
							mousePressedWrapper(event, canvas, data))
	root.bind("<Key>", lambda event:
							keyPressedWrapper(event, canvas, data))
	timerFiredWrapper(canvas, data)
	# and launch the app
	root.mainloop()  # blocks until window is closed
	print("bye!")

run(400, 200)