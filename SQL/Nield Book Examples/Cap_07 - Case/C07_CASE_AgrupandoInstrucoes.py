# Introduação à Linguagem SQL (Nield)
# Capítulo 05 - Pág. 55 à 63


# Libraries

import sqlite3



# Programa

print(f"\n **** SQL - Capítulo 07 **** \n")


SourceFile = "weather_stations.db"

conn = sqlite3.connect(SourceFile)
curs = conn.cursor()


read_query = """SELECT year,
                CASE
                    WHEN wind_speed >= 40 THEN "high"
                    WHEN wind_speed >= 30 THEN "moderate"
                    ELSE "low"

                END as wind_severity,

                COUNT(*) as record_count
                FROM station_data
                GROUP BY 1, 2
             """


curs.execute(read_query)
Info = curs.fetchall()

print(f" p66. {Info} \n")


# Closing

curs.close()
conn.close()
print("")
