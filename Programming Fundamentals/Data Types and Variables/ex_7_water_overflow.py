number_of_lines = int(input())

poured_liters = 0
for i in range(number_of_lines):
    liters_of_water = int(input())
    poured_liters += liters_of_water
    if poured_liters > 255:
        poured_liters -= liters_of_water
        print("Insufficient capacity!")
print(poured_liters)



# number_of_lines = int(input())

# poured_liters = 0
# for i in range(number_of_lines):
#     liters_of_water = int(input())
#     if poured_liters + liters_of_water <= 255:
#         poured_liters += liters_of_water
#         continue
#     print("Insufficient capacity!")
# print(poured_liters)