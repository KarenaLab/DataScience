
from sql_joins_v01 import *


left = [1, 2, 3, 4, 5]
right = [4, 5, 6, 7]

print(f" >   left list = {left}")
print(f" >  right list = {right} \n")

l_join = left_join(left, right)
print(f" >    left join: {l_join}")

i_join = inner_join(left, right)
print(f" >   inner join: {i_join}")

r_join = left_join(right, left)
print(f' > "right_join": {r_join}')

o_join = outter_join(left, right)
print(f" >  outter join: {o_join}\n")


