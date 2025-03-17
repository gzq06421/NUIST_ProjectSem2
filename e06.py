try:
    age = int(input("input your age"))
    if age <= 19:
        print("student account")
    elif 20 <= age <= 54:
        print("not available")
    else:
        print("elderly account")
except ValueError:
    print("Error , input a correct integer")
