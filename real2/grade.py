# print("成大資工營")
mid = float(input("請輸入期末考成績："))
final = float(input("請輸入期末考成績："))
 
hw = input("請輸入所有作業成績，成績間隔用空白鍵：")
hw_list = hw.split() # 什麼都不傳就代表從空白鍵切割
# print(hw_list) # 可以 print() 出來看看
hw = [float(grade) for grade in hw_list]
 
avg_hw = sum(hw)/ len(hw) # 這裡也有改動
grade = (mid * 0.3) + (final * 0.3) + (avg_hw * 0.4)
grade **= 0.5 # 縮寫
grade *= 10 # 縮寫
 
print(grade)
'''
#function版本
def my_sum(hw_list):
    sum = 0
    for hw_grade in hw_list:
        sum += hw_grade
    return sum
 
hw = [100, 0, 97]
hw.append(98)
hw.append(60)
 
print("請輸入期中考成績：", end="")
mid = float(input())
final = float(input("請輸入期末考成績："))
 
avg_hw = my_sum(hw)/ len(hw) # 這裡也有改動
grade = (mid * 0.3) + (final * 0.3) + (avg_hw * 0.4)
grade **= 0.5 # 縮寫
grade *= 10 # 縮寫
 
print(grade)
'''
'''
#for迴圈版本
hw = [100, 0, 97]
hw.append(98)
hw.append(60)
 
print("請輸入期中考成績：", end="")
mid = float(input())
final = float(input("請輸入期末考成績："))
 
sum = 0 
for hw_grade in hw:
    sum += hw_grade
avg_hw = sum / len(hw) # 這裡也有改動
grade = (mid * 0.3) + (final * 0.3) + (avg_hw * 0.4)
grade **= 0.5 # 縮寫
grade *= 10 # 縮寫
 
print(grade)
'''
'''
# 這是第四代
hw = [100, 0, 97]
hw.append(98)
hw.append(60)

mid = float(input("請輸入期中考成績："))
final = float(input("請輸入期末考成績："))

avg_hw = sum(hw) / len(hw) # 這裡也有改動
grade = (mid * 0.3) + (final * 0.3) + (avg_hw * 0.4)
grade **= 0.5 # 縮寫
grade *= 10 # 縮寫
 
print(grade)
'''
'''
這是第一代
mid = 78.5
final = 88

hw1 = 100
hw2 = 0
hw3 = 97
avg_hw = (hw1 + hw2 + hw3) / 3

grade = (mid * 0.3) + (final * 0.3) + (avg_hw * 0.4)
grade **= 0.5 # 縮寫
grade *= 10 # 縮寫
print(grade)
'''

'''
這是第二代
hw1 = 100
hw2 = 0
hw3 = 97
 
print("請輸入期中考成績：", end="")
mid = float(input())
final = float(input("請輸入期末考成績："))
 
avg_hw = (hw1 + hw2 + hw3) / 3
grade = (mid * 0.3) + (final * 0.3) + (avg_hw * 0.4)
grade **= 0.5 # 縮寫
grade *= 10 # 縮寫
 
print(grade)
'''
'''
這是第三代
hw = [100, 0, 97] #這裡有改動
 
print("請輸入期中考成績：", end="")
mid = float(input())
final = float(input("請輸入期末考成績："))
 
avg_hw = (hw[0] + hw[1] + hw[2]) / 3 # 這裡也有改動
grade = (mid * 0.3) + (final * 0.3) + (avg_hw * 0.4)
grade **= 0.5 # 縮寫
grade *= 10 # 縮寫
 
print(grade)
'''
'''
好處不只少打字，還可以推廣
如果要新增成績
例如：變成有 5 個 hw 成績
hw = [100, 0, 97]
hw.append(98)
hw.append(60)
'''