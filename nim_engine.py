from random import randint

max_bunches = 5
max_size = 20

holder = {}
sorted_keys = None


def put_stones():
    global holder, sorted_keys
    holder = {}
    for i in range(1, max_bunches + 1):
        holder[i] = randint(1, max_size)
    sorted_keys = sorted(holder.keys())


def take_from_bunch(pos, qnt):
    if pos in holder:
        holder[pos] -= qnt
        return True
    else:
        return False


def get_brunches():
    res = []
    for key in sorted_keys:
        res.append(holder[key])
    return res


def is_over():
    return sum(holder.values()) == 0


put_stones()
print(get_brunches())
take_from_bunch(1,2)
print(get_brunches())
print(is_over())