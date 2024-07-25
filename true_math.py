from math import inf

def divide(first, second):
    if second == 0:
        return inf
    else:
        return first / second

#
# #проверка функции на работоспособность
#
# result1 = divide(10, 2)
# result2 = divide(4, 0)
#
# print(result1)
# print(result2)
