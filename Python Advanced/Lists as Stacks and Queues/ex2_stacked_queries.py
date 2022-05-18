s = []
number = int(input())

for _ in range(number):
    query = [int(x) for x in input().split()]
    command = query[0]
    if command == 1:
        new_number = query[1]
        s.append(new_number)
    elif command == 2:
        if s:
            s.pop()
    elif command == 3:
        if s:
            print(max(s))
    elif command == 4:
        if s:
            print(min(s))

reversed_numbers = []
while s:
    value = str(s.pop())
    reversed_numbers.append(value)
print(", ".join(reversed_numbers))
