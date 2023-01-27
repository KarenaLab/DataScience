
from sql_joins_v01 import *


left = [1, 2, 3, 4, 5, 6]
right = [4, 5, 6, 7, 8]

print(f" >  left list = {left}")
print(f" > right list = {right} \n")

i_join = inner_join(left, right)
print(f" >  inner join: {i_join}")

l_join = left_join(left, right)
print(f" >   left join: {l_join}")

o_join = outter_join(left, right)
print(f" > outter join: {o_join} \n")
