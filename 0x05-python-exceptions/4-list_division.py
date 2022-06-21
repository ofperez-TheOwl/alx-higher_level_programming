#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i, j = 0, 0
    result = []
    while i < list_length:
        try:
            j = my_list_1[i] / my_list_2[i]
            result.append(j)
        except TypeError:
            print("wrong type")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            i = i + 1
    return (result)
