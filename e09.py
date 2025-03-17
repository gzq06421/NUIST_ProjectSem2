def factorial_for(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


try:
    num = int(input("input a number: "))
    print(factorial_while(num))
except ValueError:
    print("Error , input a correct integer")