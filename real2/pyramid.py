def myprint(content,time):
    for i in range(time):
        print(content,end='')
def draw(h):
    for i in range(h):
        myprint(' ',h-1-i)
        print('X',end='')
        if i:
            print('O',end='')
            myprint('O',2*(i-1))
        if i:
            print('X',end='')
        myprint(' ',h-1-i)
        print()

draw(int(input("請輸入塔高：")))