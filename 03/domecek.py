from turtle import forward, left, exitonclick
from math import sqrt

stena = 150
odvesna = sqrt(2)*stena
strecha = odvesna/2

forward(stena)
left(90)
forward(stena)
left(45)
forward(strecha)
left(90)
forward(strecha)
left(45)
forward(stena)
left(90)
forward(stena)
left(135)
forward(odvesna)
left(225)
forward(stena)
left(225)
forward(odvesna)

exitonclick()