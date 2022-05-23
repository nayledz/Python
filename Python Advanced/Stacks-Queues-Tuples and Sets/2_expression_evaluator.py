from collections import deque

expression = input().split()

operators = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b,
}
queue = deque()
for ch in expression:
    if ch in operators:
        result = queue.popleft()
        while queue:
            number = queue.popleft()
            result = operators[ch](result, number)
        queue.append(result)
    else:
        queue.append(int(ch))

print(queue.popleft())
