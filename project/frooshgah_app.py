from pyfiglet import Figlet
font = Figlet(font="standard")
print(font.renderText("KAJ STORE"))

def menu():
    print("1== add product")
    print("2== edit product")
    print("3== delete product")
    print("4== search product")
    print("5== show list")
    print("6== buy product")
    print("7== exit")

q = True
while q:

    product = open("product.txt" , "r")
    product_list = product.read()
    product_file = product_list.split("\n")

    PRODUCT = []

    for i in range(len(product_file)):
        product_info = product_file[i].split(",")
        my_dict = {}
        my_dict["id"] = product_info[0]
        my_dict["name"] = product_info[1]
        my_dict["price"] = product_info[2]
        my_dict["count"] = product_info[3]
        PRODUCT.append(my_dict)

    print(PRODUCT)
    menu()

    user = int(input())

    if user == 1:
        def add():
            ID = input("enter product id==")
            name = input("enter product name==")
            price = input("enter product price==")
            count = input("enter product count==")
            b = open("product.txt" , "a")
            b.write("\n"+ID+","+name+","+price+","+count)
            b.close()
        add()
    elif user == 2:
        def edit():
            for j in range(len(PRODUCT)):
                print(PRODUCT[j]["name"])

            name = input("enter the product name==")

            for i in range(len(PRODUCT)-1):
                print(i)
                if name == PRODUCT[i]["name"]:
                    PRODUCT.pop(i)
            ID = input("Enter  product id==")
            name = input("Enter your product name==")
            price = input("Enter your product price==")
            count = input("Enter your product quantity==")
            dict_ed = {"id":ID,"name":name,"price":price,"count":count}
            PRODUCT.append(dict_ed)
            pr = ""
            for g in range(len(PRODUCT)):
                pr += PRODUCT[g]["id"] + "," + PRODUCT[g]["name"] + "," + PRODUCT[g]["price"] + "," + PRODUCT[g]["count"] 
                if g != len(PRODUCT)-1:
                    pr += "\n"
            myfile = open("product.txt" , "w")
            myfile.write(pr)
            myfile.close()
        edit()
    elif user == 3:
        pass
    elif user == 4:
        def search():
            user_4 = input("do you want to search with id or name?")
            if user_4 == "nmae":
                p_n = input("enter product name==") 
                for i in range(len(PRODUCT)):
                    if PRODUCT[i]["name"] == p_n:
                        print("product detaile==")
                        print("id==",PRODUCT[i]["id"])
                        print("name==",PRODUCT[i]["name"])
                        print("price==",PRODUCT[i]["price"])
                        print("count==",PRODUCT[i]["count"])
                    else :
                        print("cant find the product")
            elif user_4 == "id":
                p_i = input("enter product id==") 
                for j in range(len(PRODUCT)):
                    if PRODUCT[j]["id"] == p_i:
                        print("product detaile==")
                        print("id==",PRODUCT[j]["id"])
                        print("name==",PRODUCT[j]["name"])
                        print("price==",PRODUCT[j]["price"])
                        print("count==",PRODUCT[j]["count"])
                    else :
                        print("cant find the product")
        search()
    elif user == 5:
        def lst():
            z = open("product.txt" , "r")
            product = open("product.txt" , "r")
            az = z.read()
            print(az)
        lst()
    elif user == 6:
        pass
    elif user == 7:
        q = False

    