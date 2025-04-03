
print("Tento program zjistí, jestli je jedno slovo obsaženo ve druhém.")

retezec1 = input("Zadej první slovo: ")
retezec2 = input("Zadej druhé slovo: ")

retezec1_lower = retezec1.lower()
retezec2_lower = retezec2.lower()

if retezec2_lower in retezec1_lower:
    print(f'"{retezec2}" je obsaženo ve slově "{retezec1}".')
elif retezec1_lower in retezec2_lower:
    print(f'"{retezec1}" je obsaženo ve slově "{retezec2}".')
else:
    print("Žádné slovo není obsaženo ve druhém.")
