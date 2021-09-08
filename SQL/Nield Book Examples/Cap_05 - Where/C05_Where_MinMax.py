# Introduação à Linguagem SQL (Nield)
# Capítulo 05 - Pág. 43 à 53


# Libraries

import sqlite3



# Programa

print(f"\n **** SQL - Capítulo 05 **** \n")


SourceFile = "weather_stations.db"

conn = sqlite3.connect(SourceFile)
curs = conn.cursor()


minyear_query = "SELECT MIN(year) FROM station_data"

curs.execute(minyear_query)
Min = curs.fetchall()[0][0]

maxyear_query = "SELECT MAX(year) FROM station_data"

curs.execute(maxyear_query)
Max = curs.fetchall()[0][0]

i = Min

while(i <= Max):

    read_query = f"SELECT COUNT(*) FROM station_data WHERE year= {i}"
    curs.execute(read_query)
    Size = curs.fetchall()[0][0]
    print(f" Year = {i}, Count = {Size}")

    i = i+1


print("")


# Closing

curs.close()
conn.close()
print("")






