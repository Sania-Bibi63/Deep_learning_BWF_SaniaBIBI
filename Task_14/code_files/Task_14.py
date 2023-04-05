import pandas as pd
import sqlite3
# csv
print("csv")
csv_file = pd.read_csv(r'c:\Users\HP\Desktop\csv_file.csv')
print(csv_file.head())
print("------------------------------------")


# JSON 
print("Json")
Json_file = pd.read_json(r'c:\Users\HP\Desktop\Json_file.json',typ='series')
print(Json_file.head())
print("------------------------------------")


# Excel 
print("Excel")
data = pd.read_excel(r'c:\Users\HP\Desktop\Excel_file.xlsx')
print(data.head())
print("------------------------------------")

#  sql
print("sql")
import sqlite3
import pandas as pd
import sqlite3
conn=sqlite3.connect('test_database')
c=conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS product ([product_id] INTEGER PRIMARY KEY,[product_name]TEXT,[price]INTEGER)''')

c.execute(''' INSERT OR IGNORE INTO product (product_id, product_name,price)VALUES(1,'bed',800),(2,'Printer',200),(3,'mobile',300),(4,'Desk',450),(5,'Chair',150)''')
conn.commit() 
df=pd.read_sql_query('SELECT * from product',conn)  
print(df)
print("-----------------------------------")
df = pd.DataFrame(df, columns = ['product_id', 'product_name', 'price'])
print (df)    

