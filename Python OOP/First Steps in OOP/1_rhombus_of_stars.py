def get_line(i, n):
    space_count = n - 1 - i
    stars_count = i + 1
    return ' ' * space_count + ('* ' * stars_count).strip()


def print_rhombus(n):
    for i in range(0, n, 1):
        print(get_line(i, n))
    for i in range(n - 2, -1, -1):
        print(get_line(i, n))

number = int(input())
print_rhombus(number)
print_rhombus(4)