# Introduação à Linguagem SQL (Nield)
# Capítulo 05 - Pág. 43 à 53


# Libraries

import sqlite3



# Programa

print(f"\n **** SQL - Capítulo 05 **** \n")


SourceFile = "weather_stations.db"

conn = sqlite3.connect(SourceFile)
curs = conn.cursor()


read_query = "SELECT count(*) FROM station_data WHERE length(report_code) != 6"

curs.execute(read_query)
Info = curs.fetchall()[0][0]

print(f" p48: Error Count: {Info}")


read_query = "SELECT * FROM station_data WHERE report_code LIKE 'A%'"

curs.execute(read_query)
Info = curs.fetchall()[0][0]

print(f" p48: Starts with A: {Info}")


read_query = "SELECT * FROM station_data WHERE report_code LIKE 'B_C%'"

curs.execute(read_query)
Info = curs.fetchall()[0][0]

print(f" p48:   Like 'B_C%': {Info}")


# Closing

curs.close()
conn.close()
print("")

