import sqlite3

db = sqlite3.connect('C:\\Users\\DEMIRKAN\Desktop\\veritabani.db')

imlec =db.cursor()

#komut = """INSERT INTO ABC VALUES (3,5,10,12,12,20)"""
  
#imlec.execute(komut)
#db.commit()

komut1 = "SELECT * FROM ABC where ID=2"

imlec.execute(komut1)

veriler = imlec.fetchall()
print(veriler)
print(veriler[0][2])