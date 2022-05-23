first_input = set([int(x) for x in input().split()])
second_input = set([int(x) for x in input().split()])
number = int(input())

for _ in range(number):
    command = input().split()
    numbers = [int(num) for num in (command[2::])]
    if command[0] == "Add" and command[1] == "First":
        [first_input.add(int(num)) for num in (command[2::])]
    elif command[0] == "Add" and command[1] == "Second":
        [second_input.add(int(num)) for num in (command[2::])]
    elif command[0] == "Remove" and command[1] == "First":
        first_input = set(first_input.difference(numbers))
    elif command[0] == "Remove" and command[1] == "Second":
        second_input = set(second_input.difference(numbers))
    else:
        print(first_input.issubset(second_input) or second_input.issubset(first_input))

first_input = [(str(x)) for x in sorted(first_input)]
second_input = [(str(x)) for x in sorted(second_input)]

print(', '.join(first_input))
print(', '.join(second_input))