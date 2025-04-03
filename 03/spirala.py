from turtle import forward, left, speed, exitonclick

print("Tento program ti vykreslí kruhovou spirálu.")

speed(5)
sides = 100

# Nakreslení n-uhelnik
length = sides / sides
angle = 180 * (1 - 2 / sides)
for i in range(1000):
    forward(length)
    left(180 - angle)
    

exitonclick()
