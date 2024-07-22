import csv
a = []
with open('trainingdata.txt', newline='') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        a.insert(0, (float(row[0]), float(row[1])))

a = sorted(a, key=lambda b: b[0])
b = float(input())
c = 0
while c < len(a) and b > a[c][0]:
    c += 1

if(c >= len(a)):
    print(a[len(a)-1][1])
else:
    d = a[c-1][0]
    e = a[c][0]
    f = a[c-1][1]
    g = a[c][1]
    
    h = (b - d) / (e - d)
    i = (g - f) * h
    print((i + f))
