import db


def insert(name,qty,price):
    try:
        db.cursor.execute("SELECT qty FROM product where name=%s",(name,))
        result = db.cursor.fetchone()
        if result:
            db.cursor.execute("UPDATE product SET qty = qty + %s,price=%s WHERE name=%s",(qty,price,name))
            print("*"*12)
            print(f"Updated {name} ")
            print("*"*12)
        else:
            # If item does not exist, insert it as a new item
            db.cursor.execute("INSERT INTO product (name, qty, price) VALUES (%s, %s, %s)",(name, qty, price))
            print(f"Added {name} to inventory.")

        db.conn.commit()



    except Exception as e:

        print("OOPS!! SOMETHING WENT WRONG ..")

        print(f"Error: {e}")

        db.conn.rollback()

def readall():
    try:
        db.cursor.execute("SELECT NAME,QTY,PRICE FROM product ")
        data=db.cursor.fetchall()
        print("     NAME \t   |QUANTITY  |PRICE ")
        print("-" * 40)
        for row in data:
            name, qty, price = row
            print(f"{name:^15}|{qty:^10}|{price:^10}")

    except:
        print("Something went wrong")

# def update(name,qty,price):
#     db.cursor.execute("SELECT name FROM product WHERE name = %s",(name,))
#     result=db.cursor.fetchall()
#     if result:
#         db.cursor.execute("")

def update_item(name,qty,price):
    try:
        # Ask for product details to update

        # Update query for quantity or price, based on user input
        if qty:
            db.cursor.execute("UPDATE product SET QTY = %s WHERE NAME = %s", (qty, name))
        if price:
            db.cursor.execute("UPDATE product SET PRICE = %s WHERE NAME = %s", (price, name))

        # Commit changes to the database
        db.conn.commit()

        print("Item updated successfully!")

    except Exception as e:
        print("Something went wrong:", e)

def delete_item(name):
    try:
        db.cursor.execute("SELECT * FROM product WHERE NAME = %s", (name,))
        data = db.cursor.fetchone()

        if data:
            db.cursor.execute("DELETE FROM product WHERE NAME = %s", (name,))
            db.conn.commit()
            print(f"Item '{name}' deleted successfully!")
        else:
            print(f"No item named '{name}' found in the database.")

    except Exception as e:
        print("Something went wrong:", e)





