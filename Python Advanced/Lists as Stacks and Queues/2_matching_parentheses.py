expression = input()

s = []

for ch in range(len(expression)):
    value = expression[ch]
    if value == "(":
        s.append(ch)
    elif value == ")":
        start_index = s.pop()
        end_index = ch
        print(expression[start_index:end_index + 1])

