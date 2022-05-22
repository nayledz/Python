from collections import deque
bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
intelligence_value = int(input())

earned_price = intelligence_value
current_barrel_size = gun_barrel_size
while locks:
    if len(bullets) == 0:
        break
    current_lock = locks[0]
    current_bullet = bullets[-1]
    if current_lock >= current_bullet:
        locks.popleft()
        bullets.pop()
        print("Bang!")
    else:
        bullets.pop()
        print("Ping!")
    earned_price -= bullet_price
    current_barrel_size -= 1
    if current_barrel_size <= 0 < len(bullets):
        current_barrel_size += gun_barrel_size
        print("Reloading!")

if not locks:
    print(f'{len(bullets)} bullets left. Earned ${earned_price}')
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")