char_index = int(input())
index_last_ch = int(input())

for i in range(char_index, index_last_ch + 1):
    character = chr(i)
    print(character, end=" ")