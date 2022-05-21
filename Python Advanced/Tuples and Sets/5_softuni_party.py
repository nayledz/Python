number_of_guests = int(input())

vip_guests = set()
regular_guests = set()

for _ in range(number_of_guests):
    reservation_code = input()
    if reservation_code[0].isdigit():
        vip_guests.add(reservation_code)
    else:
        regular_guests.add(reservation_code)

while True:
    command = input()
    if command == "END":
        break
    else:
        guest = command
        if guest in vip_guests:
            vip_guests.remove(guest)
        elif guest in regular_guests:
            regular_guests.remove(guest)

print(len(vip_guests) + len(regular_guests))
[print(x) for x in sorted(vip_guests)]
[print(x) for x in sorted(regular_guests)]