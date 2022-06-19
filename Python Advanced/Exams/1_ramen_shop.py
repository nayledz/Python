from collections import deque

bowls_of_ramen = [int(x) for x in input().split(', ')]
customers = deque([int(x) for x in input().split(', ')])

while customers and bowls_of_ramen:
    current_bowl = bowls_of_ramen[-1]
    current_customer = customers[0]

    if current_customer == current_bowl:
        bowls_of_ramen.pop()
        customers.popleft()
        continue

    if current_bowl > current_customer:
        bowls_of_ramen[-1] -= current_customer
        customers.popleft()

    if current_customer > current_bowl:
        customers[0] -= current_bowl
        bowls_of_ramen.pop()

if not customers:
    print("Great job! You served all the customers.")
    if bowls_of_ramen:
        bowls_of_ramen = [str(x) for x in bowls_of_ramen]
        print(f"Bowls of ramen left: {', '.join(bowls_of_ramen)}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    customers = [str(x) for x in customers]
    print(f"Customers left: {', '.join(customers)}")