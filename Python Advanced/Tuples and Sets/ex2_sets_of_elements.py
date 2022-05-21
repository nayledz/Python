n, m = [int(x) for x in input().split()]

first_set = set()
second_set = set()

[first_set.add(int(input())) for _ in range(n)]
[second_set.add(int(input())) for _ in range(m)]

result_set = first_set.intersection(second_set)
[print(x) for x in result_set]