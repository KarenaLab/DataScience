# Introduação à Linguagem SQL (Nield)
# Capítulo 05 - Pág. 43 à 53


# Libraries

import sqlite3



# Programa

print(f"\n **** SQL - Capítulo 05 **** \n")


SourceFile = "weather_stations.db"

conn = sqlite3.connect(SourceFile)
curs = conn.cursor()

read_query = "SELECT COUNT(*) from station_data WHERE year BETWEEN 2005 AND 2010"

curs.execute(read_query)
Info = curs.fetchall()[0][0]

print(f" Measurements between 2005 and 2010 = {Info} [using between]")


read_query = "SELECT COUNT(*) from station_data WHERE year >= 2005 and year <=2010"

curs.execute(read_query)
Info = curs.fetchall()[0][0]

print(f" Measurements between 2005 and 2010 = {Info} [using operators and logic]")

print("")


# Closing

curs.close()
conn.close()
print("")









