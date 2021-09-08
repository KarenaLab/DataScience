# Introduação à Linguagem SQL (Nield)
# Capítulo 05 - Pág. 43 à 53


# Libraries

import sqlite3



# Programa

print(f"\n **** SQL - Capítulo 05 ****")
print("")
print(f" > SQLite Version: {sqlite3.sqlite_version}")
print(f" > Module Version: {sqlite3.version} \n")


SourceFile = "weather_stations.db"

conn = sqlite3.connect(SourceFile)
curs = conn.cursor()

count_query = "SELECT COUNT(*) FROM station_data"

curs.execute(count_query)
Size = curs.fetchall()[0][0]

print(f" > p.43: All Registers = {Size}")


count_query = "SELECT COUNT(*) FROM station_data WHERE year= 2010"

curs.execute(count_query)
Size = curs.fetchall()[0][0]

print(f" > p.44: All 2010 Registers = {Size}\n")


read_query = "SELECT * FROM station_data WHERE year= 2010"

curs.execute(read_query)
Info = curs.fetchall()


read_query = "SELECT COUNT(*) FROM station_data WHERE year BETWEEN 2005 and 2010"

curs.execute(read_query)
Info  = curs.fetchall()[0][0]

print(f" > p.45: All BETWEEN 2005 and 2010 Registers = {Info}\n")


# Closing

curs.close()
conn.close()
print("")






