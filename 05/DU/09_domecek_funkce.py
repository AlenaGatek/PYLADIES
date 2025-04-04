from turtle import forward, left, penup, pendown, speed, setpos, exitonclick
from math import sqrt

def vykresli_domecek(stena):
    odvesna = sqrt(2)*stena
    strecha = odvesna/2
    mezera = 70

    for i in range(1):
        pendown()
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
        left(135)
        penup()         
        forward(mezera)
        pendown() 

vykresli_domecek(30)
vykresli_domecek(40)
vykresli_domecek(80)

exitonclick()
