def perfect_numbers(num):
    current_sum = 0
    for i in range(1, num):
        if num % i == 0:
            current_sum += i
    if current_sum == num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number = int(input())
perfect_numbers(number)