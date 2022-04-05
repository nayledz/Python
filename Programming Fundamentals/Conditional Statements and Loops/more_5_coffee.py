command = input()
list = ["coding", "cat", "dog", "movie"]
counter = 0
while command != "END":
    string = command.lower()
    if string in list:
        if command.isupper():
            counter += 2
        else:
            counter += 1
    command = input()
if counter > 5:
    print('You need extra sleep')
else:
    print(counter)


