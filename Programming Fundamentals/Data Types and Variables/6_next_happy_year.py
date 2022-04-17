number = int(input()) + 1

while len(set(str(number))) != len(str(number)):
    number += 1
print(number)
