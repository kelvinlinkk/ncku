import random
 
random_number = random.randint(1, 100)
 
num = int(input("請輸入一個整數："))
 
if num == random_number:
    print("答對了")
elif num > random_number:
    print("你有點大")
elif num < random_number:
    print("你有點小")