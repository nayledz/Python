from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])

matches = 0
while males and females:
    current_male = males[-1]
    current_female = females[0]

    if current_female <= 0:
        females.popleft()
        continue
    if current_male <= 0:
        males.pop()
        continue
    if current_female % 25 == 0:
        females.popleft()
        females.popleft()
        continue
    if current_male % 25 == 0:
        males.pop()
        males.pop()
        continue

    if current_female == current_male:
        matches += 1
        males.pop()
    else:
        males[-1] -= 2
    females.popleft()

print(f"Matches: {matches}")
if males:
    males = reversed([str(x) for x in males])
    print(f"Males left: {', '.join(males)}")
else:
    print("Males left: none")

if females:
    females = [str(x) for x in females]
    print(f"Females left: {', '.join(females)}")
else:
    print("Females left: none")

