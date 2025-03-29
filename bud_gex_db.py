import mysql.connector

db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='3171996',

)

cursorObject=db.cursor()

cursorObject.execute("CREATE DATABASE bud_gex_db")
print("DONE!")