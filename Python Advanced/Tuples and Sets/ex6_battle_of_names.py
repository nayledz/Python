number = int(input())

odd = set()
even = set()

for row in range(1, number + 1):
    name = input()
    result = int(sum([ord(ch) for ch in name]) / row)
    if result % 2 == 0:
        even.add(result)
    else:
        odd.add(result)
if sum(odd) == sum(even):
    final_set = odd.intersection(even)
elif sum(odd) > sum(even):
    final_set = odd.difference(even)
elif sum(even) > sum(odd):
    final_set = odd.symmetric_difference(even)

print(', '.join(str(x) for x in final_set))