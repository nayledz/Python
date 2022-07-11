def shopping_cart(*args):
    my_dict = {
        "Pizza": [],
        "Soup": [],
        "Dessert": []
    }
    for arg in args:
        if arg == "Stop":
            sorted_dict = sorted(my_dict.items(), key=lambda x: (-len(x[1]), x[0]))
            result = ''

            if len(sorted_dict[0][1]) == 0 and len(sorted_dict[1][1]) == 0 and len(sorted_dict[2][1]) == 0:
                result = 'No products in the cart!'
            else:
                for elements in sorted_dict:
                    sorted_elements = sorted(elements[1])
                    result += f'{elements[0]}:\n'
                    for el in sorted_elements:
                        result += f' - {el}\n'
            return result

        meal = arg[0]
        product = arg[1]

        if meal == "Pizza" and len(my_dict["Pizza"]) == 4:
            continue
        if meal == "Soup" and len(my_dict["Soup"]) == 3:
            continue
        if meal == "Dessert" and len(my_dict["Dessert"]) == 2:
            continue

        if product not in my_dict[meal]:
            my_dict[meal].append(product)


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))



print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))


print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
