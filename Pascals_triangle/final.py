file = open("triangle.txt", "r")
file2 = open("answers.txt", "w")
rows = [50, 60, 68, 2017, 2468, 3000, 4000, 4234, 5000, 6000, 8000]
filerows = []

for i in range(11):
    filerows.append(file.readline().split(","))

def getrow(n):
    row = filerows[rows.index(n)]
    return row

def triangle(n,k):
    row = getrow(n)
    return int(row[k])

def main(n,p):
    sumation=0
    #print "n = " + str(n)
    #print "p = " + str(p)
    for k in range(min(n+1-p,2*p)):
        #print k
        sumation += triangle(n,p+k)*triangle(2*p,k)
    return sumation

trials = [[50,30],[4234,4000],[3000,1234],[2017,34],[4000,3000],[5000,3000]]
answers = []
total =[]

for row in filerows:
    total.append([])
    for i in row:
        total[-1]+=int(i)
    print total[-1]

for trial in trials:
    print "TRIAL = " + str(trial)
    answers.append(main(trial[0],trial[1])%(10**9+7))
    
for answer in answers:
    file2.write(str(answer) + "\n")