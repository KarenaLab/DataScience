# Introduação à Linguagem SQL (Nield)
# Capítulo 05 - Pág. 43 à 53


# Libraries

import sqlite3



# Programa

print(f"\n **** SQL - Capítulo 05 **** \n")


SourceFile = "weather_stations.db"

conn = sqlite3.connect(SourceFile)
curs = conn.cursor()

read_query = "SELECT COUNT(*) from station_data WHERE month= 3 OR month= 6 OR month= 9 OR month= 12"

curs.execute(read_query)
Info = curs.fetchall()[0][0]

print(f" Measurements for months = 3 or 6 or 9 or 12 = {Info}")


read_query = "SELECT COUNT(*) from station_data WHERE month IN (3, 6, 9, 12)"

curs.execute(read_query)
Info = curs.fetchall()[0][0]

print(f" Measurements for months in (3, 6, 9, 12) = {Info}")


# Closing

curs.close()
conn.close()
print("")











