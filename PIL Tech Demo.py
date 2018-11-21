# PIL Basics
# from PIL import Image
# 
# im1 = Image.open("pickleRick.png") # import image
# im1.show() # opens the image in Preview
# 
# im1Size = im1.size # returns size of thet image
# print(im1Size) # --> (605, 800)
# 
# im2 = im1.rotate(45) # rotate image by 45 degrees counter-clockwise
# im2.show() 
# im2.save("im2.png") # saves the new image in the same directory
# 
# 
# # Creating Pixel Map
# img = Image.new("RGB", (255, 255), "black")
# pixels = img.load() # 
# for i in range(img.size[0]):
#     for j in range(img.size[1]):
#         newPixel = (i, j, 100)
#         pixels[i, j] = newPixel    
# img.show()

## Using Images from within Tkinter

# Converts PIL image object into Tkinter photo object 
# im_tk = ImageTk.PhotoImage(im1)

# Draw the image on the Canvas using converted image                                                                                                                                                                                                                                                                                   
# canvas.create_image(x1, y1, x2, y2, image=im_tk)

from tkinter import *
from PIL import Image, ImageTk, ImageDraw


# im1 = Image.open("bread.png")
# #print("size:", im1.size)
# im_tk = ImageTk.PhotoImage(im1)


def init(data):
    #data.im1 = Image.open("bread.png")
    #data.size = data.im1.size # returns tuple (250, 250)
    data.im_tk = ImageTk.PhotoImage(Image.open("bread.png"))
    data.cX = data.width//2
    data.cY = data.height//2
    data.move = 10
    data.change = 25

def mousePressed(event, data):
    pass

def keyPressed(event, data):
    if event.keysym == "Up":
        data.cY -= data.move
    elif event.keysym == "Left":
        data.cX -= data.move
    elif event.keysym == "Down":
        data.cY += data.move
    elif event.keysym == "Right":
        data.cX += data.move
    elif event.keysym == "r":
        data.cX = data.width//2
        data.cY = data.height//2
    elif event.keysym == "s":
        # newSize = (data.size[0]-data.change, data.size[1]-data.change)
        # data.im1.resize((newSize))
        data.im_tk.rotate(45)


def redrawAll(canvas, data):
    #canvas.create_image(cX, cY, image=filename)
    canvas.create_image(data.cX, data.cY, image=data.im_tk)

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

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
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
    redrawAll(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(400, 400)