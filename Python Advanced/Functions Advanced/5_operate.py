def operate(sign, *args):
    result = args[0]
    calc = {'+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b if b != 0 else a

    }
    for num in args[1:]:
        result = calc[sign](result, num)
    return result

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))