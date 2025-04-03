from turtle import forward, left, speed, exitonclick

print("Tento program ti vykreslí n-úhelník")
sides = int(input("Zadej počet stran: "))

speed(5)

# Nakreslení n-uhelnik
length = 200 / sides
angle = 180 * (1 - 2 / sides)
for i in range(sides):
    forward(length)
    left(180 - angle)

exitonclick()