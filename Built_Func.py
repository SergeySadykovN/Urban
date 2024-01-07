def summ_list(*args):
    import math
    print(f'summ: {math.fsum(args)}')
    print(f'average value: {math.fsum(args)/len(args)}')
    print(f'max value: {max(args)}')
    print(f'min value: {min(args)}')


def find_same_value(list1, list2):
    list_same_values = []
    for i in list1:
        if i in list2:
            list_same_values.append(i)
    print(f'The same values is : {list_same_values}')





