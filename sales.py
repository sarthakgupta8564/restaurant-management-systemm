import db
import datetime as dt
import uuid
import qrcode
import os

order=[]
items=[]
total_bill = 0
order_number = 1
def place_order():
    global total_bill,items

    try:

        while True:
            name = input("Enter name of the item (or type 'done' to finish) : ")
            if name.lower() == 'done':
                break

            qty_requested = int(input(f"Enter the Quantity of '{name}' :"))
            db.cursor.execute("SELECT qty,price FROM product WHERE name = %s",(name,))
            result = db.cursor.fetchone()
            if result:
                avail_qty,price = result
                if (qty_requested <= avail_qty):
                    new_qty = avail_qty - qty_requested
                    total_amt = qty_requested * price
                    db.cursor.execute("UPDATE product SET qty= %s WHERE name = %s",(new_qty,name))
                    db.conn.commit()
                    items.append((name,qty_requested,price,total_amt))
                    total_bill = total_bill + total_amt

                    print(f"{qty_requested} x {name} is placed successfully (sub_total = ₹{total_bill}) 💸")

                else :
                    print(f"SORRY! ONLY {avail_qty} ITEMS ARE AVAILABLE FOR '{name}'. ")
            else:
                print(f"SORRY! ITEM NAME '{name}' IS NOT FOUND")
    except ValueError:
        print("INVALID INPUT!,QUANTITY MUST BE A NUMBER.")
    except Exception as e:
        print("Something Went Wrong: ",e)










def dispaly_bill():
    global total
    total = 0
    for i in order:
        total += i['qty']*i['price']

    print("*"*10,"YOUR BILL BOSS","*"*10)
    print(f"NAME \t\t  QUANTITY \t\t\t PRICE \t\t")
    for i in order:
        print(f"{i['name']}\t\t {i['qty']} \t\t\t\t{i['price']}")
    print("_"*40)
    print(" "*25,"total =",total)
    print("_" * 40)


def generate_payment_qr(total_amount):
    upi_id = "kanha37357@oksbi"
    payee_name = "Sarthak Gupta"

    # Create the UPI payment link
    upi_link = f"upi://pay?pa={upi_id}&pn={payee_name.replace(' ', '%20')}&am={total_amount}&cu=INR"

    # Generate QR Code
    qr = qrcode.make(upi_link)
    qr.save("payment_qr.png")
    qr.show()

    print(f"QR Code generated for ₹{total_amount} payment!")


def payment(customer_name,total_amount):
    generate_payment_qr(total_amount)


    bill_amt = int(input("****ENTER THE AMOUNT YOU HAVE PAID **** \n "))
    if bill_amt == total_amount:
        print("IN",payment.upper()," MODE BY",customer_name.upper(),"*"*15,"ENJOY YOUR MEAL",customer_name.upper())
        # print(d.sales)
        order.clear()
        print(db.sales)
    elif (bill_amt > total):
        print("take the remaining",bill_amt-total)
    else:
        print(total-bill_amt , "MORE NEED TO PAY")











