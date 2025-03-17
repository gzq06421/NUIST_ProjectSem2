import random

random_num = random.randint(1, 10)
while True:
    try:
        guess = int(input("guess a nunber between 1~10: "))
        if guess == random_num:
            print("corect")
            break
        else:
            print("You fail, try again")
    except ValueError:
        print("Error , input a correct integer.")
