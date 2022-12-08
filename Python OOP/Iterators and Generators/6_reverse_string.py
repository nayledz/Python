def reverse_text(string):
    index = len(string) - 1
    while index > -1:
        yield string[index]
        index -= 1


for char in reverse_text("step"):
    print(char, end='')
