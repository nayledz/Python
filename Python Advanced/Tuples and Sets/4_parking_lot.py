number = int(input())

parking = set()
for n in range(number):
    direction, car_number = input().split(', ')
    if direction == "IN":
        if car_number not in parking:
            parking.add(car_number)
    elif direction == "OUT":
        if car_number in parking:
            parking.remove(car_number)

[print(el) for el in parking]
if not parking:
    print("Parking Lot is Empty")