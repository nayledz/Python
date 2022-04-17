number_of_snowballs = int(input())

max_value = 0
best_snowball_data = 0
for i in range(number_of_snowballs):
    snowball_weight = int(input())
    time_needed = int(input())
    snowball_quality = int(input())
    value_of_snowball = (snowball_weight / time_needed) ** snowball_quality
    if value_of_snowball > max_value:
        max_value = value_of_snowball
        best_snowball_data = f"{snowball_weight} : {time_needed} = {int(max_value)} ({snowball_quality})"
print(best_snowball_data)