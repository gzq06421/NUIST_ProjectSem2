def factorial_while(num):
    result = 1
    while num > 0:
        result *= num
        num -= 1
    return result


try:
    num = int(input("input a number: "))
    print(factorial_while(num))
except ValueError:
    print("Error , input a correct integer")
