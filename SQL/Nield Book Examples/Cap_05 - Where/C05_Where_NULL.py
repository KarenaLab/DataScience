# Introduação à Linguagem SQL (Nield)
# Capítulo 05 - Pág. 43 à 53


# Libraries

import sqlite3



# Programa

print(f"\n **** SQL - Capítulo 05 **** \n")


SourceFile = "weather_stations.db"

conn = sqlite3.connect(SourceFile)
curs = conn.cursor()


read_query = "SELECT count(*) FROM station_data WHERE snow_depth IS NULL"

curs.execute(read_query)
Info = curs.fetchall()[0][0]

print(f" p50. Snow = NULL Count: {Info}")


read_query = "SELECT count(*) FROM station_data WHERE precipitation <= 0.5"

curs.execute(read_query)
Info = curs.fetchall()[0][0]

print(f" p51. Precipitation >= 0.5 Count*: {Info}")


read_query = "SELECT count(*) FROM station_data WHERE precipitation IS NULL OR precipitation <= 0.5"

curs.execute(read_query)
Info = curs.fetchall()[0][0]

print(f" p51. Precipitation >= 0.5 Count: {Info}")


read_query = "SELECT count(*) FROM station_data WHERE coalesce(precipitation, 0) <= 0.5"

curs.execute(read_query)
Info = curs.fetchall()[0][0]

print(f" p51. Precipitation >= 0.5 Count: {Info}")



# Closing

curs.close()
conn.close()
print("")

