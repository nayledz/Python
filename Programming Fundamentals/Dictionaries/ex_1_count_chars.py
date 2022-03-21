# string = input().split(" ")
# characters = {}
#
# for word in string:
#     for ch in word:
#         if ch not in characters:
#             characters[ch] = 0
#         characters[ch] += 1
#
# for (key, value) in characters.items():
#     print(f"{key} -> {value}")

from collections import Counter
word = input()
result = Counter(word)

for key, value in result.items():
    if key != ' ':
        print(f"{key} -> {value}")