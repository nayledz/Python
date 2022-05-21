from itertools import combinations
string_of_numbers = [int(x) for x in input().split()]
target_number = int(input())

iterations = 0
unique_pairs = set()

for first, second in combinations(string_of_numbers, 2):
    iterations += 1
    if first + second == target_number:
        unique_pairs.add((first, second))
        print(f'{first} + {second} = {target_number}')
print(f'Iterations done: {iterations}')
if unique_pairs:
    [print(f"({first}, {second})") for first, second in unique_pairs]


