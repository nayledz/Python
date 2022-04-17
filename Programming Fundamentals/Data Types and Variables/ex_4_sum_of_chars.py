number_of_lines = int(input())

sum = 0
for i in range(number_of_lines):
    letter_per_line = input()
    sum += ord(letter_per_line)
print(f"The sum equals: {sum}")