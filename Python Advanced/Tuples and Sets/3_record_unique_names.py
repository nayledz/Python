n = int(input())
name_list = set()

for _ in range(n):
    name = input()
    name_list.add(name)

[print(el) for el in name_list]