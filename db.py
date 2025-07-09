import mysql.connector
conn = mysql.connector.connect(host="localhost",user="root",password="8839998564",database="cafe")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS product (pid INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20) NOT NULL, qty INT NOT NULL , price INT NOT NULL )")

cursor = conn.cursor(buffered=True)


db=[]
sales=[]
customer=[]
