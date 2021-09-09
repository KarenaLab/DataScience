# Introduação à Linguagem SQL (Nield)
# Capítulo 05 - Pág. 55 à 63


# Libraries

import sqlite3



# Programa

print(f"\n **** SQL - Capítulo 06 **** \n")


SourceFile = "weather_stations.db"

conn = sqlite3.connect(SourceFile)
curs = conn.cursor()


read_query = "SELECT year, month, COUNT(*) FROM station_data WHERE tornado= 1 GROUP BY year, month ORDER BY year, month"

curs.execute(read_query)
Info = curs.fetchall()

print(f" p58. Tornardo Counting (by year): {Info} \n")


# Closing

curs.close()
conn.close()
print("")
