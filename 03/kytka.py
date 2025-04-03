from turtle import forward, left, right, speed, exitonclick

print("Tento program ti nakreslí kytku i s listy a stonkem")

speed(0)

left(90)
forward(50)
left(90)

delka = 30
uhel = 1

for i in range(10):
    forward(delka)
    right(uhel)
    uhel = uhel + 1

print(uhel)
uhel_back = 180 - (2*uhel)
left(uhel_back)


for j in range(10):
    forward(delka)
    right(uhel)    
    uhel = uhel + 1

exitonclick()