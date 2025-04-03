from turtle import forward, left, speed, exitonclick

print("Tento program ti vykreslí ornament - úhlová spirála.")

speed(5)

sides = 8
length = 1 / sides
angle = 180 * (1 - 2 / sides)
for i in range(52):
    forward(length)
    left(180 - angle)
    length = length + 1
    andgle = angle + 10

exitonclick()