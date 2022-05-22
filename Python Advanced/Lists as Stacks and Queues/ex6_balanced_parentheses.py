from collections import deque
input_line = input()

queue = deque()
parentheses = {
    '(': ')',
    '{': '}',
    '[': ']'
}

is_balanced = True
for el in input_line:
    if el in "{[(":
        queue.append(parentheses[el])
    else:
        if not queue or el != queue.pop():
            is_balanced = False
            print("NO")
            break
        else:
            is_balanced = True
if is_balanced:
    print("YES")

