from turtle import forward, penup, left, pendown, speed, exitonclick

speed(5)

# Nakreslení pětiúhelníku
sides = 5
length = 200 / sides
angle = 180 * (1 - 2 / sides)
for i in range(sides):
    forward(length)
    left(180 - angle)

penup()
forward(150)
pendown()

# Nakreslení šestiúhelníku
sides = 6
length = 200 / sides
angle = 180 * (1 - 2 / sides)
for i in range(sides):
    forward(length)
    left(180 - angle)

penup()
forward(150)
pendown()

# Nakreslení sedmiúhelníku
sides = 7
length = 200 / sides
angle = 180 * (1 - 2 / sides)
for i in range(sides):
    forward(length)
    left(180 - angle)

penup()
forward(150)
pendown()

# Nakreslení osmiúhelníku
sides = 8
length = 200 / sides
angle = 180 * (1 - 2 / sides)
for i in range(sides):
    forward(length)
    left(180 - angle)

exitonclick()