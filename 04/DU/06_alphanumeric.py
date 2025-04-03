#Nakonec jsem snad našla jak si upravit vkládání více řádků v cmd

import unicodedata

print("Kolik písmen je v textu tvé oblíbené písně?")

print("Zadej text tvé oblíbené písně. Pro ukončení vkládání zařádkuj:")

# Načítání víceřádkového textu
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

# Spojení všech řádků do jednoho textu
text = "\n".join(lines)

# Počítání písmen 
text_lower = text.lower()
pocet = 0

for pismeno in text_lower:
    if pismeno.isalnum() == True:
        pocet = pocet + 1

print(f'Ve tvé písni je {pocet} písmen.')