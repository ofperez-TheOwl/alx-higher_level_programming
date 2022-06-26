#!/usr/bin/python3
def weight_average(my_list=[]):
    if (my_list is None or len(my_list) == 0):
        return (0)
    total_score, total_weight = 0, 0
    for i in my_list:
        total_score = total_score + i[0] * i[1]
        total_weight = total_weight + i[1]
    return (total_score / total_weight)
