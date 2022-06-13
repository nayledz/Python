def even_odd(*args):
    command = args[-1]
    parity = 0 if command == "even" else 1
    result = []
    for el in args[:-1]:
        if el % 2 == parity:
            result.append(el)
    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))