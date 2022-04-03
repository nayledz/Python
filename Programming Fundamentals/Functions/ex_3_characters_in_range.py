def ch_in_range(ch1, ch2):
    for i in range(ord(ch1) + 1, ord(ch2)):
        print(chr(i), end = " ")


first_character = input()
second_character = input()
ch_in_range(first_character, second_character)