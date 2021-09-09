# Introduação à Linguagem SQL (Nield)
# Capítulo 05 - Pág. 55 à 63


# Libraries

import sqlite3



# Programa

print(f"\n **** SQL - Capítulo 06 **** \n")


SourceFile = "weather_stations.db"

conn = sqlite3.connect(SourceFile)
curs = conn.cursor()


read_query = """SELECT month, round(AVG(temperature),2)
                FROM station_data WHERE year >= 2000 GROUP BY month
             """

curs.execute(read_query)
Info = curs.fetchall()

print(f"{Info} \n")


read_query = """SELECT year, round(SUM(snow_depth),3), round(SUM(precipitation),3), MAX(precipitation)
                FROM station_data WHERE year >= 2000 GROUP BY year
             """

curs.execute(read_query)
Info = curs.fetchall()

print(f"{Info} \n")


# Closing

curs.close()
conn.close()
print("")
