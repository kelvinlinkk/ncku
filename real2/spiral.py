a = []
size = 3
endNum = size ** 2
x = -1
y = 0
count = 2
step = size-1
for i in range(size):
    a.append([])
    for j in range(size):
        a[i].append(1)
        print(a[i][j], end='\t')
    print('\n')
