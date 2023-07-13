from random import randint
def rotation(mLen):
    a = []
    b = []
    for i in range(mLen):
        a.append([])
        b.append([])
        for j in range(mLen):
            a[i].append(randint(-1000,1000))
            print(a[i][j], end='\t')
        print('\n')

    print("順時針旋轉90度\n")

    for i in range(mLen):
        for j in range(mLen):
            b[i].append(a[mLen-j-1][i])
            print(b[i][j], end='\t')
        print('\n')
    return b

print(rotation(int(input("輸入陣列大小"))))
