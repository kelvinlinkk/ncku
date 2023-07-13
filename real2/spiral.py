from random import randint
a = []
size = 4
count = 1
x,y=0,-1    

# 碰撞法

for i in range(size):
    a.append([])
    for j in range(size):
        a[i].append(None)
        print(a[i][j], end='\t')
    print()

while True:
    while y+1<size and a[x][y+1]==None:
        y+=1
        a[x][y] = count
        count+=1
    while x+1<size and a[x+1][y]==None:
        x+=1
        a[x][y] = count
        count+=1
    while y-1>=0 and a[x][y-1]==None:
        y-=1
        a[x][y] = count
        count+=1
    while x-1>=0 and a[x-1][y]==None:
        x-=1
        a[x][y] = count
        count+=1
    if count >= 17:
        break

'''
01 02 03 04
12 13 14 05
11 16 15 06
10 09 08 07
'''

for i in range(size):
    for j in range(size):
        print(a[i][j], end='\t')
    print()