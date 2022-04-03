def odd_even_sum(num):
    even_sum = 0
    odd_sum = 0
    for i in num:
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


number = map(int, list(input()))
odd_even_sum(number)
