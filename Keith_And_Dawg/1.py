from PIL import Image
im = Image.open("image1.png")
pix = im.load()
count = 0
for x in range(400):
    for y in range(400):
        pix[x,y] = (pix[x,y][0],pix[x,y][1],pix[x,y][2],255)
        if pix[x,y][0] != 0:
            print pix[x,y][0]
            count+=1
print count
im.save("image1V2.png")
