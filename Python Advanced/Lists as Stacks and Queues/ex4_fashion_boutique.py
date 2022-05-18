box_of_clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

rack_count = 1
current_capacity = rack_capacity

while box_of_clothes:
    value = box_of_clothes[-1]
    if value > current_capacity:
        rack_count += 1
        current_capacity = rack_capacity
    else:
        current_capacity -= value
        box_of_clothes.pop()
print(rack_count)