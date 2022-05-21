numbers = [float(x) for x in input().split(' ')]

count_dict = {}
count = 0
for num in numbers:
    if num not in count_dict:
        count_dict[num] = 1
    else:
        count_dict[num] += 1
for key, value in count_dict.items():
    print(f"{key} - {value} times")