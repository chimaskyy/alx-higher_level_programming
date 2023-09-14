#!/usr/bin/python
def weight_average(my_list=[]):
    if not my_list:
        return 0
    score = sum(map(lambda x: x[0] * x[1], my_list))
    weight = sum(x[1] for x in my_list)
    return score / weight
