import collections
text = input()

occurrences = {}

for ch in text:
    if ch not in occurrences:
        occurrences[ch] = 1
    else:
        occurrences[ch] += 1

ordered_occurrences = collections.OrderedDict(sorted(occurrences.items()))
for key, value in ordered_occurrences.items():
    print(f"{key}: {value} time/s")