from collections import deque
substrings = deque(input().split())

main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]
collection = []

while substrings:
    if len(substrings) > 1:
        if (substrings[0] + substrings[-1]) in main_colors or (substrings[0] + substrings[-1]) in secondary_colors:
            collection.append((substrings[0] + substrings[-1]))
        elif (substrings[-1] + substrings[0]) in main_colors or (substrings[-1] + substrings[0]) in secondary_colors:
            collection.append((substrings[-1] + substrings[0]))
        else:
            substrings[0] = substrings[0][:-1]
            substrings[-1] = substrings[-1][:-1]
            index = len(substrings)//2

            if len(substrings[0]) > 0 and len(substrings[-1]) > 0:
                substrings.insert(index, substrings[0])
                substrings.insert(index + 1, substrings[-1])

            elif len(substrings[0]) > 0:
                substrings.insert(index, substrings[0])

            elif len(substrings[-1]) > 0:
                substrings.insert(index, substrings[-1])

        substrings.pop()
        substrings.popleft()
    else:
        if substrings[0] in main_colors or substrings[0] in secondary_colors:
            collection.append(substrings[0])
            substrings.pop()
        break

if "orange" in collection:
    if "red" not in collection or "yellow" not in collection:
        collection.remove("orange")

if "purple" in collection:
    if "red" not in collection or "blue" not in collection:
        collection.remove("purple")

if "green" in collection:
    if "yellow" not in collection or "blue" not in collection:
        collection.remove("green")

print(collection)