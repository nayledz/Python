def rounds_numbers(new_list):
    current_list = list()
    for num in new_list:
        current_list.append(round(float(num)))
    return current_list


numbers = input().split(" ")


print(rounds_numbers(numbers))