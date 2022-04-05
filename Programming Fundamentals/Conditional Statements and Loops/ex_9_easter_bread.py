budget = float(input())
price_1kg_flour = float(input())

price_pack_eggs = 0.75 * price_1kg_flour
price_1l_milk = price_1kg_flour + (0.25 * price_1kg_flour)
price_needed_milk = price_1l_milk / 4
needed_budget_for_one_bread = price_pack_eggs + price_needed_milk + price_1kg_flour

needed_budget = 0
colored_eggs = 0
number_of_bread = 0
while budget >= needed_budget_for_one_bread:
    colored_eggs += 3
    number_of_bread += 1
    if number_of_bread % 3 == 0:
        colored_eggs -= (number_of_bread - 2)
    budget -= needed_budget_for_one_bread
print(f"You made {number_of_bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
