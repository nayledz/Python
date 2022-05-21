number = int(input())

unique_compounds = set()
for _ in range(number):
    chemical_compounds = input().split()
    [unique_compounds.add(el) for el in chemical_compounds]

[print(x) for x in unique_compounds]

