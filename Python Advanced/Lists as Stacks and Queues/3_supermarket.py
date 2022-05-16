from collections import deque
q = deque()

while True:
    command = input()
    if command == "End":
        print(f"{len(q)} people remaining.")
        break
    elif command == "Paid":
        for person in range(len(q)):
            print(q.popleft())
    else:
        q.append(command)