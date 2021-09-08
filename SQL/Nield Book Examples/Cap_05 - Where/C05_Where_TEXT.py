# Introduação à Linguagem SQL (Nield)
# Capítulo 05 - Pág. 43 à 53


# Libraries

import sqlite3



# Programa

print(f"\n **** SQL - Capítulo 05 **** \n")


SourceFile = "weather_stations.db"

conn = sqlite3.connect(SourceFile)
curs = conn.cursor()


read_query = "SELECT * FROM station_data WHERE report_code = '513A63'"

curs.execute(read_query)
Info = curs.fetchall()

print(f"Report Info: {Info}\n")


read_query = "SELECT * FROM station_data WHERE report_code IN ('513A63', '1F8A7B', 'EF616A')"

curs.execute(read_query)
Info = curs.fetchall()

print(f"Report Info: {Info}\n")


read_query = "SELECT * FROM station_data WHERE report_code IN ('513A63')"

curs.execute(read_query)
Info = curs.fetchall()

print(f"Report Info: {Info}\n")


# Closing

curs.close()
conn.close()
print("")





