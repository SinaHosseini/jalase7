import qrcode

PRODUCTS = []
last_change = []


def read_from_database():
    f = open("vscode/database.txt", "r")

    for line in f:
        result = line.split(",")
        my_dict = {"code": result[0], "name": result[1],
                   "price": result[2], "count": result[3]}
        PRODUCTS.append(my_dict)

    f.close()


def write_to_database():
    f = open("vscode/database.txt", "w")

    for line in PRODUCTS:
        convert_D_to_L = []
        convert_D_to_L.append(line["code"])
        convert_D_to_L.append(line["name"])
        convert_D_to_L.append(line["price"])
        convert_D_to_L.append(line["count"])
        last_change.append(convert_D_to_L)

    f.write(str(last_change))

    f.close()


def show_menu():
    print("1.Add")
    print("2.Edit")
    print("3.Remove")
    print("4.Search")
    print("5.Show List")
    print("6.Buy")
    print("7.convert product to qr")
    print("8.exit")


def add():
    code = input("enter code: ")
    name = input("enter name: ")
    price = input("enter price: ")
    count = input("enter count: ")
    new_product = {'code': code, 'name': name, 'price': price, 'count': count}
    PRODUCTS.append(new_product)
    print("Add successful\n")


def edit():
    choice = input("enter product code or 2.exit: ")
    for product in PRODUCTS:
        if product["code"] == choice:
            user_input = int(
                input("1.name\n2.price\n3.count\n4.exit\nenter your choice: "))
            if user_input == 1:
                product["name"] = input("enter new name: ")
                print("\nUpdate Successful\n")
                break
            elif user_input == 2:
                product["price"] = input("enter new price: ")
                print("\nUpdate Successful\n")
                break
            elif user_input == 3:
                product["count"] = input("enter new count: ")
                print("\nUpdate Successful\n")
                break
            else:
                break


def remove():
    choice = input("enter product code or 2.exitL: ")
    for product in PRODUCTS:
        if product["code"] == choice:
            choice1 = input("Are you sure?\n1.Yes\n2.No\n")
            if choice1 == "1":
                PRODUCTS.remove(product)
                print("Remove successful\n")
                break
            elif choice1 == "2":
                break


def search():
    while True:
        user_input = input("type your keyword: ")
        user_input = user_input.lower()

        if user_input == "exit":
            break
        else:
            for product in PRODUCTS:
                if product["code"] == user_input or product["name"] == user_input:
                    print(product["code"], "\t\t", product["name"],
                          "\t\t", product["price"], product["count"], "\n")
                    break
            else:
                print("not found\n")


def show_list():
    print("code\t\tname\t\tprice\t\tcount")
    for product in PRODUCTS:
        print(product["code"], "\t\t", product["name"],
              "\t\t", product["price"], "\t\t", product["count"])


def buy():
    pass


def convert_qr():
    data = []
    choice = input("enter product code or 2.exitL: ")
    for product in PRODUCTS:
        if product["code"] == choice:
            data.insert(0, product["code"])
            data.insert(1, product["name"])
            data.insert(2, product["price"])
            data.insert(3, product["count"])
            image = qrcode.make(data)
            image.save("product_image.png")
            print("Convert successful\n")


print("Welcome to store")
print("Loading...")
read_from_database()
print("Data loaded")

while True:
    print("-"*50)
    show_menu()
    choice = int(input("\nenter your choice: "))

    if choice == 1:
        add()
    elif choice == 2:
        edit()
    elif choice == 3:
        remove()
    elif choice == 4:
        search()
    elif choice == 5:
        show_list()
    elif choice == 6:
        buy()
    elif choice == 7:
        convert_qr()
    elif choice == 8:
        write_to_database()
        print("\nHave Nice Time")
        exit()
