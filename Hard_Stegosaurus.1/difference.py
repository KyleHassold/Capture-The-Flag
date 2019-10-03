from PIL import Image
im1 = Image.open("doge.png")
im2 = Image.open("edited.png")
pix1 = im1.load()
pix2 = im2.load()
count = 0
for x in range(537):
    for y in range(529):
        pix2[x,y] = (abs(pix1[x,y][0]-pix2[x,y][0]), abs(pix1[x,y][1]-pix2[x,y][1]), abs(pix1[x,y][2]-pix2[x,y][2]), 255)
        if pix2[x,y][0] > 100:
            count+=1

im2.save("difference.png")

#from PIL import Image
#im = Image.open("edited.png")
#final = Image.open("edited.png")
#pix = im.load()
#finalrgb = final.load()
#binary = ""
#
#for x in range(537):
#    for y in range(529):
#        if pix[x,y][0] % 2 == 0:
#            binary += "0"
#        else:
#            binary += "1"
#        if pix[x,y][1] % 2 == 0:
#            binary += "0"
#        else:
#            binary += "1"
#        if pix[x,y][3] % 2 == 0:
#            binary += "0"
#        else:
#            binary += "1"
#
#print binary