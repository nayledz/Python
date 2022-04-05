word = input()
listNum = []

for i in range(len(word)):
    if word[i].isupper():
        listNum.append(i)
print(listNum)