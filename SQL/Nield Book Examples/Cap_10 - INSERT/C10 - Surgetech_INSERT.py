# Introdução ao SQL
# Capítulo 10 - Gerenciando Dados


# Libraries

import sqlite3


# Program

Filename = "SurgeTechDB.db"

conn = sqlite3.connect(Filename)
curs = conn.cursor()

insert_query = """INSERT INTO attendee (first_name, last_name)
                  VALUES ("Thomas", "Nield")
               """

curs.execute(insert_query)
conn.commit()

insert_query = """ INSERT INTO attendee (first_name, last_name, phone, email, vip)
                   VALUES
                   ('Jon', 'Skeeter', '480-218-5842', 'johnskeeter@rex.net', 1),
                   ('Sam', 'Scala', '215-678-3401', 'sam.scala@gmail.com', 0),
                   ('Britanny', 'Fischer', '593-285-72961', 'britanny.fischer@outlook.com', 0)
               """

curs.execute(insert_query)
conn.commit()


read_query = "SELECT * FROM attendee"

curs.execute(read_query)
Info = curs.fetchall()
print(f"Attendee Lines:\n{Info}\n")


delete_query = "DELETE FROM attendee"

curs.execute(delete_query)
conn.commit()

curs.execute(read_query)
Info = curs.fetchall()
print(f"Attendee Lines:\n{Info}\n")





# Closing

curs.close()
conn.close()
print("")

