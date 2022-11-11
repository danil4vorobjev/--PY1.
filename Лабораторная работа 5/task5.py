import random
import string
from random import sample

count = 8

def get_random_password() -> str:

    list_ = []

    seq = string.ascii_letters + string.digits

    for i in random.sample(seq, count):
        list_.append(i)



    return list_


print(get_random_password())

