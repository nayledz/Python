def sum_numbers(a, b):
    return a + b


def subtract(current_sum, c):
    return current_sum - c


first_num, second_num, third_num = int(input()), int(input()), int(input())
print(subtract(sum_numbers(first_num, second_num), third_num))