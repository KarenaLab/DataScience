# Introdução à Linguagem SQL (Nield)
# Capítulo 04 - p.33 à 42

# Libraries

import sqlite3



# Programa

print(f"\n **** SQL - Capítulo 04 ****")
print("")
print(f" > SQLite Version: {sqlite3.sqlite_version}")
print(f" > Module Version: {sqlite3.version} \n")


SourceFile = "rexon_metals.db"

conn = sqlite3.connect(SourceFile)
curs = conn.cursor()


read_query = "SELECT * FROM product"

Reading = curs.execute(read_query)
Info = curs.fetchall()
print(Info)
print("")


read_query = "SELECT product_id, description, price FROM product"

Reading = curs.execute(read_query)
Info = curs.fetchall()
print(Info)
print("")


read_query = "SELECT product_id, description, price, price*1.07 FROM product"

Reading = curs.execute(read_query)
Info = curs.fetchall()
print(Info)
print("")


read_query = "SELECT product_id, description, price, round(price*1.07, 2) FROM product"

Reading = curs.execute(read_query)
Info = curs.fetchall()
print(Info)
print("")

read_query = "SELECT product_id, description, price, price%2 FROM product"

Reading = curs.execute(read_query)
Info = curs.fetchall()
print(Info)
print("")


# Closing

curs.close()
conn.close()
print("")
