from PIL import Image
im1 = Image.open("logo.png")
im2 = Image.open("changed.png")
pix1 = im1.load()
pix2 = im2.load()
count = 0
print pix2[995,600]
for x in range(2000):
    for y in range(1000):
        pix2[x,y] = (abs(pix1[x,y][0]-pix2[x,y][0]), abs(pix1[x,y][1]-pix2[x,y][1]), abs(pix1[x,y][2]-pix2[x,y][2]), 0)
        if pix2[x,y][0] > 100:
            count+=1

im2.save("difference.png")