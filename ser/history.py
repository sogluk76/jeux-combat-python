import cgi 
import sqlite3
import json

connection = sqlite3.connect('ma_base.db')



cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         user TEXT,
         vague TEXT,
         vie INTERGER,
         niveau INTERGER
    )
""")

dict_result= {}

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

print(form.getvalue("name"))

name = form.getvalue("name") 


print("Content-type: text/html; charset=utf-8\n")

print(form.getvalue("vie"))

vie = form.getvalue("vie") 


print("Content-type: text/html; charset=utf-8\n")

print(form.getvalue("niveau"))

niveau = form.getvalue("niveau") 

print("Content-type: text/html; charset=utf-8\n")

print(form.getvalue("vague"))

vague = form.getvalue("vague") 


connection.commit()

cursor.execute("""INSERT INTO users (user, niveau, vie, vague) VALUES (?, ?, ?, ?)
""", (name, niveau, vie, vague))
connection.commit()

cursor.execute("""SELECT * FROM users """)


names = cursor.fetchall() 


for name in names :
        dict_result[name[0]] = (
        {
            "user": name[1], 
            "vague":name[2], 
            "vie":name[3],
            "niveau":name[4]
        }
    )


json_result = json.dumps(dict_result, indent = 4)
print(json_result)


connection.commit()



connection.close()