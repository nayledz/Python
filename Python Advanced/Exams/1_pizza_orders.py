from collections import deque

pizza_orders = deque([int(x) for x in input().split(', ')])
pizza_making_employee = [int(x) for x in input().split(', ')]

pizzas = 0
while pizza_orders and pizza_making_employee:
    current_pizza_number = pizza_orders[0]
    current_employee = pizza_making_employee[-1]
    if current_pizza_number <= 0 or current_pizza_number > 10:
        pizza_orders.popleft()
        continue

    if current_pizza_number <= current_employee:
        pizzas += current_pizza_number
        pizza_orders.popleft()
        pizza_making_employee.pop()
    else:
        pizzas += current_employee
        pizza_making_employee.pop()
        pizza_orders[0] -= current_employee

if not pizza_orders and pizza_making_employee:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {pizzas}")
    pizza_making_employee = [str(x) for x in pizza_making_employee]
    print(f"Employees: {', '.join(pizza_making_employee)}")
else:
    print("Not all orders are completed.")
    pizza_orders = [str(x) for x in pizza_orders]
    print(f"Orders left: {', '.join(pizza_orders)}")