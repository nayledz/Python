country_names = input().split(", ")
capitals = input().split(", ")

result = dict(zip(country_names, capitals))
for country, capital in result.items():
    print(f"{country} -> {capital}")