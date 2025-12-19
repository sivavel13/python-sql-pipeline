import sqlite3
import pandas as pd

conn=sqlite3.connect("sales.db")
cur=conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS sales(id INTEGER, category TEXT, qty INTEGER, price REAL)")
cur.execute("DELETE FROM sales")
cur.executemany("INSERT INTO sales VALUES(?,?,?,?)",[
(1,'clothes',5,20),
(2,'electronics',2,100),
(3,'clothes',1,30)
])
conn.commit()

df=pd.read_sql_query("SELECT category, SUM(qty*price) AS revenue FROM sales GROUP BY category", conn)
df.to_csv("sql_output.csv", index=False)
print(df)
