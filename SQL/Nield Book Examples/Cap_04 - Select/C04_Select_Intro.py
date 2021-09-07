# Introdução à linguagem SQL (Nield)
# Capítulo 04 - p.33 à 42

# Libraries

import sqlite3


# Programa

print(f"\n **** SQL - Capítulo 04 ****")
print("")
print(f" > SQLite Version: {sqlite3.sqlite_version}")
print(f" > Module Version: {sqlite3.version} \n")


SourceFile = "rexon_metals.db"

conn = sqlite3.connect(SourceFile)
curs = conn.cursor()

read_query = "SELECT * FROM customer"


Reading = curs.execute(read_query)
print(".execute(): Executes an SQL statement. Values may be bound to the statement")
print("   using placeholders. execute() will only execute a single SQL statement.")
print("   If you try to execute more than one statement with it, it will raise")
print("   a Warning. Use executescript() if you want to execute multiple SQL")
print("   statements with one call.\n")
print(f"   Return: {Reading}\n\n")


Info = curs.fetchone()
print("fetchone() = Fetches the next row of a query result set, returning a single")
print("   sequence, or None when no more data is available.\n")
print(f"   Return: {Info}\n\n")


Reading = curs.execute(read_query)
Info = curs.fetchall()
print("fetchall() = Fetches all (remaining) rows of a query result, returning a")
print("    list. Note that the cursor’s arraysize attribute can affect the")
print("    performance of this operation. An empty list is returned when no rows")
print("    are available.\n")
print(f"   Return: {Info}\n\n")


Reading = curs.execute(read_query)
Info = ""
while(Info != None):
    Info = curs.fetchone()
    print(Info)


# Closing

curs.close()
conn.close()

print(f"\n * \n")
