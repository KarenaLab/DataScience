# Introduação à Linguagem SQL (Nield)

# Libraries

import sqlite3



# Programa

print(f"\n **** SQL - Capítulo 08 **** \n")


SourceFile = "rexon_metals.db"

# Inner Join
conn = sqlite3.connect(SourceFile)
curs = conn.cursor()


join_query = """ SELECT customer_order.customer_id, name AS customer_name,
                 SUM(order_qty * price) as total_revenue

                 FROM customer
                     INNER JOIN customer_order
                     ON customer.customer_id = customer_order.customer_id

                     INNER JOIN product
                     ON customer_order.product_id = product.product_id

                 GROUP BY 1,2                 
             """

curs.execute(join_query)
Info = curs.fetchall()

print(f"INNER JOIN (Somente empresas que tem pedido(s):\n{Info}\n")


join_query = """ SELECT customer_order.customer_id, name AS customer_name,
                 COALESCE(SUM(order_qty * price), 0) as total_revenue

                 FROM customer
                     LEFT JOIN customer_order
                     ON customer.customer_id = customer_order.customer_id

                     LEFT JOIN product
                     ON customer_order.product_id = product.product_id

                 GROUP BY 1,2                 
             """

curs.execute(join_query)
Info2 = curs.fetchall()

print(f"LEFT JOIN (Todas empresas e zerando valores nulos):\n{Info2}\n")


# Closing

curs.close()
conn.close()





