numbers = [int(x) for x in input().split()]

reversed_string = []
while numbers:
    value = numbers.pop()
    reversed_string.append(str(value))
print(" ".join(reversed_string))