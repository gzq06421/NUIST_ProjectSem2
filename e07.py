babyNames = ["Martha", "Magda", "Mandy", "Missy", "Marsha"]
for name in babyNames:
    print(name + " Smith")

new_name = input("add new name: ")
babyNames.append(new_name)
for name in babyNames:
    print(name + " Smith")
