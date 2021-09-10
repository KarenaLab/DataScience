# Introduação à Linguagem SQL (Nield)

# Libraries

import sqlite3



# Programa

print(f"\n **** SQL - Capítulo 08 **** \n")


SourceFile = "rexon_metals.db"

# Inner Join
conn = sqlite3.connect(SourceFile)
curs = conn.cursor()


join_query = """ SELECT order_id, [customer.customer_id], name AS customer_name,
                 street_address, city, state, zip, order_date, product.product_id,
                 description, order_qty, (order_qty * price) AS revenue

                 FROM customer
                     INNER JOIN customer_order
                     ON customer_order.customer_id = customer.customer_id

                     INNER JOIN product
                     ON customer_order.product_id = product.product_id                 
             """

curs.execute(join_query)
Info = curs.fetchall()

print(f"{Info}\n")



# Closing

curs.close()
conn.close()





