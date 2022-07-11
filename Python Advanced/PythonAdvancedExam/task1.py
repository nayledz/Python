from collections import deque

size_egg = deque([int(x) for x in input().split(', ')])
paper_size = [int(x) for x in input().split(', ')]

box = 0
while size_egg and paper_size:
    current_egg = size_egg[0]
    current_paper = paper_size[-1]

    if current_egg <= 0:
        size_egg.popleft()
        continue

    if current_egg == 13:
        size_egg.popleft()
        paper_size[0], paper_size[-1] = paper_size[-1], paper_size[0]
        continue

    if current_egg + current_paper <= 50:
        box += 1
        size_egg.popleft()
        paper_size.pop()
    else:
        size_egg.popleft()
        paper_size.pop()

if box > 0:
    print(f"Great! You filled {box} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if size_egg:
    size_egg = [str(el) for el in size_egg]
    print(f"Eggs left: {', '.join(size_egg)}")

if paper_size:
    paper_size = [str(el) for el in paper_size]
    print(f"Pieces of paper left: {', '.join(paper_size)}")



