from collections import deque
quantity_of_food = int(input())
quantity_per_order = deque([int(x) for x in input().split()])

print(max(quantity_per_order))

is_succeeded = True
while quantity_per_order:
    if quantity_per_order[0] > quantity_of_food:
        is_succeeded = False
        break
    else:
        quantity_of_food -= quantity_per_order[0]
        quantity_per_order.popleft()

if is_succeeded:
    print("Orders complete")
else:
    quantity_per_order = [str(x) for x in quantity_per_order]
    print(f"Orders left: {' '.join(quantity_per_order)}")
