from PIL import Image

img1 = Image.open("pickleRick.png")
img1.show()

# img1Size = img1.size # --> (605, 800)
# print(img1Size)
# 
# img1_2 = img1.resize((300,400))
# img1_2.show()
# 
# img2 = img1.rotate(90)
# # img2.show()

im1Size = img1.size
print(im1Size)

img2 = img1.resize((300,400))
img2.show()

ro = img2.rotate(40)
ro.show()



### 
TP1

-manipulate images within game
-start writing code
     -actually work
