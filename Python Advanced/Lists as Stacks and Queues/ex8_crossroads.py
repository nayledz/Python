from collections import deque
green_light_duration = int(input())
free_window_duration = int(input())

cars = deque()
command = input()
passed_counter = 0
crashed = False

while not crashed:
    if command == "END":
        break
    if command == "green":
        current_green = green_light_duration
        while cars and current_green > 0:
            car = cars.popleft()
            if current_green + free_window_duration >= len(car):
                passed_counter += 1
            else:
                print('A crash happened!')
                print(f'{car} was hit at {car[current_green + free_window_duration]}.')
                crashed = True
                break
            current_green -= len(car)
    else:
        cars.append(command)

    command = input()

if not crashed:
    print('Everyone is safe.')
    print(f'{passed_counter} total cars passed the crossroads.')