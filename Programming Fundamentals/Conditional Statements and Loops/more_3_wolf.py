string = input().split(", ")
animals = string

counter = 0
animals_list = animals.reverse()
for i in range(len(animals)):
    if animals[0] == "wolf":
        print("Please go away and stop eating my sheep")
        break
    else:
        counter += 1
        if animals[i] == "wolf":
            print(f"Oi! Sheep number {counter - 1}! You are about to be eaten by a wolf!")
            break
