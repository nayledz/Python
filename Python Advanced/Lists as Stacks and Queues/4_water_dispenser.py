from collections import deque
water_quantity = int(input())

q = deque()
while True:
    input_line = input()

    if input_line == "End":
        print(f"{water_quantity} liters left")
        break

    elif input_line == "Start":
        while q:
            command = input()
            if command == "End":
                break
                
            elif "refill" in command:
                command = command.split(" ")
                refill = int(command[1])
                water_quantity += refill
            else:
                liters = int(command)
                if water_quantity - liters >= 0:
                    water_quantity -= liters
                    print(f"{q.popleft()} got water")

                else:
                    print(f"{q.popleft()} must wait")
    else:
        q.append(input_line)

