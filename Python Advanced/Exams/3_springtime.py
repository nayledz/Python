def start_spring(**kwargs):
    my_dict = {}
    for key, value in kwargs.items():
        if value in my_dict:
            my_dict[value].append(key)
        else:
            my_dict[value] = [key]

    sorted_dict = sorted(my_dict.items(), key=lambda x: ((-len(x[1])), x[0]))

    result = ''
    for elements in sorted_dict:
        sorted_elements = sorted(elements[1])
        result += f'{elements[0]}:\n'
        for el in sorted_elements:
            result += f'-{el}\n'

    return result


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))
