# Introduação à Linguagem SQL (Nield)
# Capítulo 05 - Pág. 43 à 53


# Libraries

import sqlite3



# Programa

print(f"\n **** SQL - Capítulo 05 **** \n")


SourceFile = "weather_stations.db"

conn = sqlite3.connect(SourceFile)
curs = conn.cursor()


read_query = "SELECT count(*) FROM station_data WHERE tornado = 1"

curs.execute(read_query)
Info1 = curs.fetchall()

print(f" p49: Tornado Count: {Info1}")


read_query = "SELECT count(*) FROM station_data WHERE hail = 1"

curs.execute(read_query)
Info2 = curs.fetchall()

print(f" p49: Tornado Count: {Info2}")


read_query = "SELECT count(*) FROM station_data WHERE tornado = 1 and hail = 1"

curs.execute(read_query)
Info3 = curs.fetchall()

print(f" p49: Tornado Count: {Info3}")


read_query = "SELECT count(*) FROM station_data WHERE tornado = 1 or hail = 1"

curs.execute(read_query)
Info3 = curs.fetchall()

print(f" p49: Tornado Count: {Info3}")


# Closing

curs.close()
conn.close()
print("")

