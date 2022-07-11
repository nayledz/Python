def stock_availability(list, param, *args):
    if param == "delivery":
        [list.append(arg) for arg in args]

    elif param == "sell":
        if len(args) == 0:
            list.remove(list[0])
        else:
            for arg in args:
                if (str(arg)).isdigit():
                    for el in range(arg):
                        list.remove(list[0])
                else:
                    while arg in list:
                        list.remove(arg)
    return list


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
