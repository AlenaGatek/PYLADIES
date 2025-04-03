print("Kolik písmen 'K' je v textu tvé oblíbené písně?")

print("Zadej text tvé oblíbené písně. Pro ukončení vkládání zadej prázdný řádek:")

# Načítání víceřádkového textu
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

# Spojení všech řádků do jednoho textu
text = "\n".join(lines)

# Počítání písmen 'k' (bez ohledu na velikost)
pismeno = "k"
text_lower = text.lower()
pocet = text_lower.count(pismeno)

print(f'Písmeno "{pismeno}" je obsaženo v textu {pocet} krát.')