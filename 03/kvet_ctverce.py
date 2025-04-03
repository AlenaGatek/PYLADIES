from turtle import forward, left, speed, exitonclick

print("Tento program ti nakreslí kytku")
speed(0)

for i in range(18):

    for j in range(4):
        forward(50)
        left(90)

    left(20)

exitonclick()