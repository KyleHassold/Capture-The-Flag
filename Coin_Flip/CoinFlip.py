file = open("flips.txt","r")
flips = file.read()

previous = "0"
count = 0
sprees = []
final = []

for flip in flips:
    if flip == previous:
        count += 1
    else:
        sprees.append(count)
        count = 1
        previous = flip

for spree in sprees:
    while spree >= len(final):
        final.append(0)
    final[spree-1]+=1
print final

tests = ["101", "010", "1001", "0110", "10001", "01110", "100001", "011110", "1000001", "0111110", "10000001", "01111110", "100000001", "011111110", "1000000001", "0111111110", "10000000001", "01111111110", "100000000001", "011111111110", "1000000000001", "0111111111110", "10000000000001", "01111111111110", "100000000000001", "011111111111110", "1000000000000001", "0111111111111110", "10000000000000001", "01111111111111110", "100000000000000001", "011111111111111110", "1000000000000000001", "0111111111111111110", "10000000000000000001", "01111111111111111110", "100000000000000000001", "011111111111111111110", "1000000000000000000001", "0111111111111111111110", "10000000000000000000001", "01111111111111111111110"]
final = [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for test in tests:
    num = len(test)-3
    count = flips.count(test)
    final[num] += count
print final
print len(flips)
print sprees[-1]

num = 0
for i in range(len(final)):
    num += final[i]*(i+1)
print num

num = 0
for i in sprees:
    num += i
print num
    