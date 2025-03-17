import random

while True:
    random_num = random.randint(1, 10)
    try:
        guess = int(input("guess a nunber between 1~10: "))
        if guess == random_num:
            print("corect")
        else:
            print("fail,correct answer is", random_num)
        continue_game = input("go on?(y/n): ")
        if continue_game.lower() != 'y':
            break
    except ValueError:
        print("Error , input a correct integer")
