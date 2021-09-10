# Introduação à Linguagem SQL (Nield)
# Capítulo 05 - Pág. 55 à 63


# Libraries

import sqlite3



# Programa

print(f"\n **** SQL - Capítulo 07 **** \n")


SourceFile = "weather_stations.db"

conn = sqlite3.connect(SourceFile)
curs = conn.cursor()


read_query = """SELECT year, month,

                SUM(CASE WHEN tornado= 1 THEN precipitation ELSE NULL END)
                    as tornado_precipitation,

                SUM(CASE WHEN tornado= 0 THEN precipitation ELSE NULL END)
                    as non_tornado_precipitation

                FROM station_data
                GROUP BY year, month
             """


curs.execute(read_query)
Info = curs.fetchall()

print(f" p68. {Info} \n")


# Closing

curs.close()
conn.close()
print("")
