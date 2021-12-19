import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        #port="",
        user="root",
        password="",
        database = "customers"
)
mycursor = mydb.cursor()
transcations = open("customer_account_info.csv")

rows = csv.reader()

mycursor.execute("INSERT INTO data VALUES (?, ?, ?, ?)", rows)
mydb.commit()
mycursor.close()
