file = open("triangle.txt","w")

rowsLeft = 7998
newrow = "1,2,1"
needed = [50, 60, 68, 2017, 2468, 3000, 4000, 4234, 5000, 6000, 8000]

for i in range(rowsLeft):
    oldrow = newrow.split(",")
    newrow="1"
    for p in range(1,len(oldrow)):
        newrow += "," + str(int(oldrow[p])+int(oldrow[p-1]))
    newrow += ",1"
    if i+3 in needed:
        file.write(newrow)
        file.write("\n")
    if i%100 == 0:
        print i/100

