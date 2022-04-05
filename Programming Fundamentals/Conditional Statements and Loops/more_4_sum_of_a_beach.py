string = input()

count = 0
counter = 0
string_list = string.lower()
if "sand" in string_list:
    count = string_list.count("sand")
    counter += count
if "water" in string_list:
    count = string_list.count("water")
    counter += count
if "fish" in string_list:
    count = string_list.count("fish")
    counter += count
if "sun" in string_list:
    count = string_list.count("sun")
    counter += count

print(counter)