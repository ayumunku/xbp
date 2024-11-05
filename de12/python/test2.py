import random

def number_guessing_game():
    number = random.randint(1, 100)
    guess = None
    attempts = 0

    print("1から100の間の数字を当ててください！")

    while guess != number:
        guess = int(input("あなたの予想: "))
        attempts += 1

        if guess < number:
            print("もっと大きいです！")
        elif guess > number:
            print("もっと小さいです！")
        else:
            print(f"正解です！{attempts}回で当たりました！")

number_guessing_game()