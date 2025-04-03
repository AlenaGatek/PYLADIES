from turtle import forward, left, right, speed, penup, pendown, exitonclick

print("Tento program ti nakreslí správně symetrický list kytky na stonku.")

# Nastavení rychlosti kreslení
speed(0)

# Nakreslení stonku
left(90)  # Otočení želvy nahoru
forward(100)  # Nakreslení stonku
left(45)  # Příprava na kreslení listu pod správným úhlem

# Parametry listu
delka = 10  # Délka každého kroku
kroky = 20  # Počet kroků na jednu polovinu listu
zvetseni_uhel = 2  # Zvětšování úhlu pro zakřivení

# Kreslení první poloviny listu
uhel = 0
pendown()
for _ in range(kroky):
    forward(delka)
    right(zvetseni_uhel)
    uhel += zvetseni_uhel

# Otočení zpět směrem ke stonku
left(180 - uhel)

# Kreslení druhé poloviny listu (symetricky)
for _ in range(kroky):
    forward(delka)
    left(zvetseni_uhel)
    uhel -= zvetseni_uhel

# Dokončení programu
exitonclick()