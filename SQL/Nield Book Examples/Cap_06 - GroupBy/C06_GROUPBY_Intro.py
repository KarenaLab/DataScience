# Introduação à Linguagem SQL (Nield)
# Capítulo 05 - Pág. 55 à 63


# Libraries

import sqlite3



# Programa

print(f"\n **** SQL - Capítulo 06 **** \n")


SourceFile = "weather_stations.db"

conn = sqlite3.connect(SourceFile)
curs = conn.cursor()


read_query = "SELECT COUNT(*) AS record_count FROM station_data"

curs.execute(read_query)
Info = curs.fetchall()[0][0]

print(f" p55. Counting: {Info}")


read_query = "SELECT COUNT(*) AS record_count FROM station_data WHERE tornado= 1;"

curs.execute(read_query)
Info = curs.fetchall()[0][0]

print(f" p55. Tornado Counting: {Info}")


read_query = "SELECT COUNT(*) AS record_count FROM station_data WHERE tornado=  1 GROUP BY year"

curs.execute(read_query)
Info = curs.fetchall()

print(f" p55. Tornardo Counting (by year): {Info}")


# Closing

curs.close()
conn.close()
print("")



