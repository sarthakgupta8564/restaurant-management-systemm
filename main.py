import inventory as i
import sales as s
import products as prod
print("-"*40)
print("———•Restaurant Management System🍴———".center(40))


print("-"*40)
print("-"*40)

print("Welcome To Our Cafe".center(40))
print("-"*40)
# print()



def main():
    running=True
    while running:
        # print("-" * 40)
        print("CHOOSE ONE OF THE FOLLOWING OPTION")
        print("1. INVENTORY (to add item)")
        print("2. SALES  (to buy item)")
        print("3. REPORT (to see report)")
        print("4. EXIT")
        print("-" * 40)

        print()
        choice=int(input("ENTER YOUR OPTION : "))
        match choice:
            case 1:
                inventory=True
                while inventory:
                    print("-" * 40)
                    print("CHOOSE ANY ONE OF THE FOLLOWING OPTION : ")
                    print("1. ADD ITEMS ")
                    print("2. DISPLAY ITEMS ")
                    print("3. UPDATE ITEMS ")
                    print("4. DELETE ITEMS ")
                    print("5. EXIT FROM INVENTORY ")
                    print("-" * 40)

                    print()
                    option = int(input("ENTER YOUR CHOSEN OPTION : "))
                    match option:
                        case 1 :
                            name=input("ENTER THE NAME OF THE ITEM : ")
                            qty=int(input("ENTER THE QUANTITY OF THE ITEM : "))
                            price=float(input("ENTER THE PRICE THE THIS ITEM : "))
                            sales=0
                            i.insert(name,qty,price,sales)

                            print()
                        case 2. :
                            print()
                            print("MENU CARD".center(40))
                            1
                            print("-" * 40)
                            # print("*"*40)
                            i.display()


                            print("*" * 40)
                            print("-" * 40)

                            print()

                        case 3. :
                            name = input("Enter the name of the product to update: ")
                            qty = input("Enter the new quantity (or press Enter to skip): ")
                            price = input("Enter the new price (or press Enter to skip): ")

                            i.update(name , qty, price)


                            print()

                        case 4:
                            name=input("ENTER THE NAME OF THE ITEM")
                            i.delete(name)

                        case _:
                            inventory=False
            case 2:
                sales = True
                while sales:
                    print("ENTER ONE OF THE FOLLOWING OPTION ")
                    print("1. PLACE AN ORDER")
                    print("2. DISPLAY THE BILL")
                    print("3. PAY THE BILL ")
                    print("4. EXIT ")
                    print()

                    option=int(input("ENTER ANY ONE OF THE FOLLOWING OPTION : "))
                    match option:
                        case 1:
                            print("-"*15,"MENU CARD","-"*15)
                            print()
                            i.display()
                            print()
                            print()


                            s.place_order()




                        case 2:
                            s.dispaly_bill()

                        case 3 :
                            customer_name= input("PLEASE ENTER YOUR NAME:")
                            total_amount = int(input("Amount That You Have To PAY"))
                            # payment=input("HOW DO YOU WANT TO PAY \n 1. CASH \n 2. MOBILE PAY \n 3.CREDIT/DEBIT CARD\n")
                            s.payment(customer_name,total_amount)
                            print()

                        case _ :

                            sales = False
            case _:
                running=False

if __name__=="__main__":
    main()












