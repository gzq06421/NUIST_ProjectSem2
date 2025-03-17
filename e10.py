shopping_list = ["bread", "milk", "cheese", "eggs"]

while True:
    print("\nMenu:")
    print("1. Add new item:")
    print("2. Delete item:")
    print("3. Print list")
    print("4. exist")
    choice = input("请输入你的选择: ")

    if choice == '1':
        new_item = input("What's the name: ")
        shopping_list.append(new_item)
    elif choice == '2':
        item_to_delete = input("Which one: ")
        if item_to_delete in shopping_list:
            shopping_list.remove(item_to_delete)
        else:
            print("Not exist.")
    elif choice == '3':
        print("List:", shopping_list)
    elif choice == '4':
        break
    else:
        print("Error, input the right name:")
