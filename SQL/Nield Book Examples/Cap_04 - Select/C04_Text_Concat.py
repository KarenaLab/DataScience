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


read_query = "SELECT name || ', ' || state FROM customer"

curs.execute(read_query)
Info = curs.fetchall()

for line in Info:
    print(line)

# Closing

curs.close()
conn.close()

print("")

