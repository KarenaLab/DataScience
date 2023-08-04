# SQL Joins [P158] -----------------------------------------------------

# Versions
# 01 - Jan 24th, 2023 - starter
# 02 -


def inner_join(left, right):
    """
    Performs **inner join** between **left** list and **right** list.

    """
    i_join = []
    for i in right:
        if(left.count(i) > 0):
            i_join.append(i)

    return i_join


def left_join(left, right):
    """
    Performs **left join** between **left** list and **right** list.
    Attention: Take care with left and right position.

    """
    l_join = []
    for i in left:
        if(right.count(i) == 0):
            l_join.append(i)

    return l_join


def outter_join(left, right):
    """
    Performs **outter join** between **left** list and **right** list.

    """
    join = left + right
    o_join = []

    for i in join:
        if(o_join.count(i) == 0):
            o_join.append(i)

    return o_join

