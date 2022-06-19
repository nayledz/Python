def naughty_or_nice_list(list, *args, **kwargs):
    nice = []
    naughty = []
    not_found = []

    for el in args:
        el = el.split('-')
        number = int(el[0])
        type = el[1]
        kid = ''
        count = 0
        for element in list:
            if element[0] == number:
                count += 1
                kid = element[1]
        if count == 1 and type == "Nice":
            nice.append(kid)
            list.pop(list.index((number, kid)))
        elif count == 1 and type == "Naughty":
            naughty.append(kid)
            list.pop(list.index((number, kid)))

    for key, value in kwargs.items():
        count = 0
        for element in list:
            if element[1] == key:
                count += 1
        if count == 1 and value == "Nice":
            nice.append(key)
            list = [x for x in list if x[1] != key]
        elif count == 1 and value == "Naughty":
            naughty.append(key)
            list = [x for x in list if x[1] != key]

    for name in list:
        not_found.append(name[1])
    result = []
    if nice:
        result.append(f"Nice: {', '.join(nice)}")
    if naughty:
        result.append(f"Naughty: {', '.join(naughty)}")
    if not_found:
        result.append(f"Not found: {', '.join(not_found)}")
    return '\n'.join(result)


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
