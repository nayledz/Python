def rectangle(length, width):
    if type(length) != int or type(width) != int:
        return "Enter valid values!"
    else:

        def area():
            ract_area = length * width
            return ract_area

        def perimeter():
            ract_perim = (2 * length) + (2 * width)
            return ract_perim
        return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"


print(rectangle(2, 10))
print(rectangle('2', 10))