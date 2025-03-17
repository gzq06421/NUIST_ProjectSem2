try:
    num = float(input("Input a number: "))
    print(num * 2)
except ValueError:
    print("Error input again")
