numbers = input().split(" ")

abs_list = list()

for num in numbers:
    abs_list.append(abs(float(num)))

print(abs_list)