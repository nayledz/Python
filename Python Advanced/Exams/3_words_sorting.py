def words_sorting(*args):
    my_dict = {}

    for word in args:
        sum = 0
        for ch in word:
            sum += ord(ch)
        my_dict[word] = sum

    sum_of_values = 0
    for key, value in my_dict.items():
        sum_of_values += value

    if sum_of_values % 2 == 0:
        sorted_dict = [f'{key} - {value}' for key, value in sorted(my_dict.items(), key=lambda x: x[0])]
    else:
        sorted_dict = [f'{key} - {value}' for key, value in sorted(my_dict.items(), key=lambda x: -x[1])]

    return '\n'.join(sorted_dict)

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
