# Introduação à Linguagem SQL (Nield)
# Capítulo 05 - Pág. 55 à 63


# Libraries

import sqlite3



# Programa

print(f"\n **** SQL - Capítulo 06 **** \n")


SourceFile = "weather_stations.db"

conn = sqlite3.connect(SourceFile)
curs = conn.cursor()


read_query = "SELECT COUNT(DISTINCT station_number) FROM station_data"

curs.execute(read_query)
Info = curs.fetchall()

print(f"{Info} \n")


read_query = "SELECT DISTINCT station_number, year FROM station_data"

curs.execute(read_query)
Info = curs.fetchall()

print(f"{Info} \n")


# Closing

curs.close()
conn.close()
print("")
