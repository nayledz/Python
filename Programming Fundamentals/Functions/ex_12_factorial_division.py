def factorial(num):
    f = 1
    if num >= 1:
        for i in range(1, num + 1):
            f = f * i
    return f


first_number = int(input())
second_number = int(input())
result = factorial(first_number) / factorial(second_number)
print(f"{result:.2f}")