from turtle import forward, left, speed, exitonclick

print("Tento program ti vykreslí pravidelný 100-úhelník")

speed(5)

# Nakreslení 100-uhelnik
sides = 100
length = 1000 / sides
angle = 180 * (1 - 2 / sides)
for i in range(sides):
    forward(length)
    left(180 - angle)

exitonclick()