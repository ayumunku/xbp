def start_adventure():
    print("あなたは暗い森の中にいます。前方に道が二つあります。")
    print("1: 右の道に進む")
    print("2: 左の道に進む")

    choice = input("どちらの道を選びますか？ (1 または 2): ")
    if choice == "1":
        mysterious_cave()
    elif choice == "2":
        enchanted_river()
    else:
        print("無効な選択です。もう一度お試しください。")
        start_adventure()

def mysterious_cave():
    print("\n右の道を進むと、巨大な洞窟の入口にたどり着きます。")
    print("1: 洞窟に入る")
    print("2: 引き返す")

    choice = input("どうしますか？ (1 または 2): ")
    if choice == "1":
        dragon_encounter()
    elif choice == "2":
        start_adventure()
    else:
        print("無効な選択です。もう一度お試しください。")
        mysterious_cave()

def enchanted_river():
    print("\n左の道を進むと、光る川が見えてきます。")
    print("1: 川を渡る")
    print("2: 川沿いに進む")

    choice = input("どうしますか？ (1 または 2): ")
    if choice == "1":
        print("\n川を渡ろうとすると、不思議な力で川が渦を巻き、あなたは吸い込まれてしまいました。ゲームオーバーです。")
    elif choice == "2":
        hidden_treasure()
    else:
        print("無効な選択です。もう一度お試しください。")
        enchanted_river()

def dragon_encounter():
    print("\n洞窟に入ると、眠っているドラゴンを見つけます。")
    print("1: そっと近づく")
    print("2: 逃げる")

    choice = input("どうしますか？ (1 または 2): ")
    if choice == "1":
        print("\nドラゴンが目を覚まし、あなたを見つけます。勇気を出して話しかけると、ドラゴンはあなたに宝物を与えました。おめでとうございます！")
    elif choice == "2":
        print("\nあなたは逃げ出し、無事に森を抜け出しました。ゲームクリアです！")
    else:
        print("無効な選択です。もう一度お試しください。")
        dragon_encounter()

def hidden_treasure():
    print("\n川沿いを進むと、隠された宝箱を見つけます。")
    print("1: 宝箱を開ける")
    print("2: そのまま進む")

    choice = input("どうしますか？ (1 または 2): ")
    if choice == "1":
        print("\n宝箱の中には金貨と宝石がたくさん！おめでとうございます！あなたは大富豪になりました！")
    elif choice == "2":
        print("\nそのまま進むと、森を抜け出しました。何も得られませんでしたが、安全に帰ることができました。")
    else:
        print("無効な選択です。もう一度お試しください。")
        hidden_treasure()

# ゲーム開始
start_adventure()