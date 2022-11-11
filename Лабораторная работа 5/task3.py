from random import randint

start = -10
stop = 10
count = 15


def get_unique_list_numbers() -> list[int]:
    list_ = []
    while len(list_) < count:
        val = randint(start,stop)
        if val not in list_:
            list_.append(val)
    #list_ = [(randint(start,stop) for _ in range(count))]
    return list_

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
