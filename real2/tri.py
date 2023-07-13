sides = input()
sides = [int(side) for side in sides.split()]
 
if len(sides) > 3 :
    print("你輸入太多數字了")
    exit()
elif len(sides) < 3: # 或直接用 if 也可以
    print("你輸入太少數字了")
    exit()
    
if sides[0] == sides[1] == sides[2]:
    print("正三角形")
elif sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
    print("等腰三角形")
elif sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2 or sides[1] ** 2 + sides[2] ** 2 == sides[0] ** 2 or sides[0] ** 2 + sides[2] ** 2 == sides[1] ** 2:
    print("直角三角形")