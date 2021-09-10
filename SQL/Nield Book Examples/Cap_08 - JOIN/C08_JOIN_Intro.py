# Introduação à Linguagem SQL (Nield)
# Capítulo 05 - Pág. 55 à 63


# Libraries

import sqlite3



# Programa

print(f"\n **** SQL - Capítulo 08 **** \n")


SourceFile = "rexon_metals.db"

# Inner Join
conn = sqlite3.connect(SourceFile)
curs = conn.cursor()


join_query = """ SELECT order_id, customer.customer_id, order_date, ship_date,
                        name, street_address, city, state, zip, product_id,
                        order_qty
                 FROM customer INNER JOIN customer_order
                 ON customer.customer_id = customer_order.customer_id """

curs.execute(join_query)
Info = curs.fetchall()

print(f"> INNER JOIN:\n{Info} \n")


# Left Join

join_query = """ SELECT order_id, customer.customer_id, order_date, ship_date,
                        name, street_address, city, state, zip, product_id,
                        order_qty
                 FROM customer LEFT JOIN customer_order
                 ON customer.customer_id = customer_order.customer_id """

curs.execute(join_query)
Info2 = curs.fetchall()

print(f"> LEFT JOIN:\n{Info2} \n")


# Closing

curs.close()
conn.close()





