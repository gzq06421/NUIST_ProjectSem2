def divide_and_remainder(num1, num2):
    quotient = num1 // num2
    remainder = num1 % num2
    print(f"result: {quotient}, remainder: {remainder}")


try:
    num1 = int(input("first number: "))
    num2 = int(input("second number: "))
    if num1 > 0 and num2 > 0:
        divide_and_remainder(num1, num2)
    else:
        print("must be integer")
except ValueError:
    print("Error input correct integer.")
