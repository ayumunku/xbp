import random
import time

def start_game():
    print("あなたは無人島で遭難しました")
    time.sleep(1)
    print("1日目。")
    print("　今日は拠点を作ります。どこに拠点を建てますか？")
    choice = input("1: 海の近く / 2: 近くの洞窟内\n>> ")

    if choice == "1":
         print("台風が直撃して拠点が壊された。　ゲームオーバー") 
    elif choice == "2":
         next_day2()
    else:
        print("無効な入力です。もう一度選んでください。")
        start_game()

def next_day2():
    print("2日目")
    print("昨日は何も食べていないのでお腹が減っている。")
    print("近くに怪しげなキノコを発見")
    choice = input("1: 食べる/2: 食べない")
   
    if choice =="1":
        death_chance=random.random()
    if death_chance<0.5: 
        print("急に目眩がしてきた。あなたは倒れました。　ゲームオーバー")
    else:
        print("意外とうまい！？")
        next_day3()
    
    

def next_day3():
    print("３日目")
    print("歩いていると古びた井戸を発見。中には水らしきものがある")
    choice=input("1:飲む/2: 飲まない")

    if choice =="1":
        death_chance=random.random()
    if death_chance<0.5: 
        print("うわ、まっっず！！！。　ゲームオーバー")
    else:
        print("生き返る〜")
        next_day4()

def next_day4():
    print("4日目")
    print("今日は疲れたので拠点で休むべきか？")
    choice=input("1: 休む/2: 休まない")

    if choice == "1":
         next_day５()
    elif choice == "2":
         print("あなたは力尽きた...　ゲームオーバー")
    else:
        print("無効な入力です。もう一度選んでください。")
        start_game()
    
# ゲームの開始
start_game()