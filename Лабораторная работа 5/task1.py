import pprint

numbers = []

for num in range(16):

    list_ = {"bin": bin(num), "dec": num, "hex": hex(num), "oct": oct(num)}

    numbers.append(list_)


pprint.pprint(numbers)