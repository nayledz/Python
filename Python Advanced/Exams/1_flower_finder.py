from collections import deque

vowels = deque(input().split())
consonants = input().split()

words = {'rose': 'rose', 'tulip': 'tulip', 'lotus': 'lotus', 'daffodil': 'daffodil'}
found_flower = False

while vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()
    for word in words.keys():
        if current_vowel in word:
            words[word] = words[word].replace(current_vowel, '')
        if current_consonant in word:
            words[word] = words[word].replace(current_consonant, '')
        if words[word] == "":
            print(f"Word found: {word}")
            found_flower = True
            break
    if found_flower:
        break

if not found_flower:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")





