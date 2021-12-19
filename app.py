from flask import Flask ,render_template , request , redirect , url_for
import mysql.connector

app = Flask(__name__)

@app.route("/" , methods = ["POST","GET"] )

def home():
   mydb = mysql.connector.connect(
        host="localhost",
        port="",
        user="root",
        password="",
        database = "mysql"
    )
    mycursor = mydb.cursor() 
    if request.method == "POST":
        cusid = request.form["fname"]
        
        mycursor.execute()
        mydb.commit()
        mycursor.close()
    return render_template("index.html")
    

def find_risk(cusid):

if __name__ == "__main__":
    app.run()
