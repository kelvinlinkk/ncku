import random
from time import sleep
import os

def drawImg(): # 繪製地圖
    pcPos = [pcData[0],pcData[1]]
    print('        0   1   2   3  ',end='')
    for i in range(4):
        print('\n      -----------------\n    ' + str(i) + ' |', end='')
        for j in range(4):
            if j == playerData[0] and i == playerData[1]:
                print(' O ', end='')
            elif j == pcPos[0] and i == pcPos[1]:
                print(' X ', end='')
            elif isLegalMove(j,i,playerData[0],playerData[1]):
                print(' . ', end='')
            else:
                print('   ', end='')
            print('|', end='')
    print('\n      -----------------')
    sleep(1)

def isLegalMove(fromX, fromY, toX, toY): # 判斷移動合法性
    # 是否在界內
    if(toX < 0 or toX >= 4 or toY < 0 or toY >= 4):
        return False
    dx = toX - fromX
    dy = toY - fromY
    # 是否受允許
    if(dx == 0 and (dy >= -2 and dy <= 2)):
        return True
    elif ((dx == -1 or dx == 1) and (dy >= -1 and dy <= 1)):
        return True
    elif ((dx >= -2 and dx <= 2) and dy == 0 ):
        return True
    else:
        return False


def pcMove(fromX, fromY):
    while True:
        desX = random.randint(0,3)
        desY = random.randint(0,3)
        if isLegalMove(fromX,fromY,desX,desY) and (playerData[0] != desX or playerData[1] != desY):
            break
    return desX, desY

pcData = [3,3,0] #x,y,sign
playerData = [0,0,0] #x,y,sign
preWinner = "玩家" #1=電腦 0=玩家
mydict = {0:"剪刀",1:"石頭",2:"布"}
# 可以用鍵值字典結合猜拳何數字

drawImg()
while 1:
    if playerData[0] == pcData[0] or playerData[1] == pcData[1]:
        if preWinner == "電腦":
            print("電腦獲勝!")
        else:
            print("玩家獲勝!")
        break
    while True:
        playerData[2] = int(input("PK方塊剪刀石頭布，你要出0=剪刀,1=石頭,2=布："))
        pcData[2] = random.randint(0,2)
        print("電腦出" + mydict[pcData[2]])
        if playerData[2] != pcData[2]:
            break
    if (playerData[2] == 0 and pcData[2] == 2) or (playerData[2] == 1 and pcData[2] == 1) or (playerData[2] == 2 and pcData[2] == 1):
        preWinner = "玩家"
    else:
        preWinner = "電腦"
    print(preWinner + "猜拳贏了\n--------------------")
    sleep(1)
    os.system('clear')
    drawImg()
    while True:
        print("PK方塊跳")
        inputX = int(input("輸入x座標:"))
        inputY = int(input("輸入y座標:"))
        if isLegalMove(playerData[0],playerData[1],inputX,inputY):
            break
        print("輸入錯誤")
    playerData[0] = inputX
    playerData[1] = inputY
    pcData[0],pcData[1] = pcMove(pcData[0],pcData[1])
    drawImg()
os.system('set /p close=\"按任意鍵關閉\"')