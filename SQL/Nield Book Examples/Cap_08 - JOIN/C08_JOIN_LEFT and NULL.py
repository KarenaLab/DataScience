# Introduação à Linguagem SQL (Nield)

# Libraries

import sqlite3



# Programa

print(f"\n **** SQL - Capítulo 08 **** \n")


SourceFile = "rexon_metals.db"

# Inner Join
conn = sqlite3.connect(SourceFile)
curs = conn.cursor()


join_query = """ SELECT customer.customer_id, name AS customer_name
                 FROM customer LEFT JOIN customer_order
                 ON customer.customer_ID = customer_order.customer_id
                 WHERE order_id IS NULL
             """

curs.execute(join_query)
Info = curs.fetchall()

print(f"{Info} \n")



# Closing

curs.close()
conn.close()





