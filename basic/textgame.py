# print("叮咚！歡迎光臨全聯福利中心！！\n你跨過了自動門，冷風彿過你的四肢，突如其來的溫差使你忍不住發抖。\n你環顧四周，發現全聯福利中心的燈光暗淡，顯得有些詭異...")

'''
print("叮咚！歡迎光臨全聯福利中心！！")
print("你跨過了自動門，冷風彿過你的四肢，突如其來的溫差使你忍不住發抖。")
print("你環顧四周，發現全聯福利中心的燈光暗淡，顯得有些詭異...")
'''

print("""叮咚！歡迎光臨全聯福利中心！！
        你跨過了自動門，冷風彿過你的四肢，突如其來的溫差使你忍不住發抖。
        你環顧四周，發現全聯福利中心的燈光暗淡，顯得有些詭異...""")
while True :
    print("""
 
------
 
你要:
1) 乾！太可怕惹！逃走！
2) 進去啊！怕屁怕！
 
------
 
""")
    selection = input()
 
    if selection == "1":
        print("廢物！掰掰！")
        exit()
    elif selection == "2":
        break
    else :
        print("你在供三小...\n")
        # continue #其實有沒有都沒差