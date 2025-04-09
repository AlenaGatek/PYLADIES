from turtle import forward, left, penup, pendown, exitonclick
from math import sqrt, atan, degrees

def vykresli_domecek(sirka, vyska):
    odvesna = sqrt(sirka**2 + vyska**2)
    print(odvesna)
    strecha = odvesna/2
    print(strecha)
    uhel = degrees(atan(vyska/sirka))
    mezera = 70

    for i in range(1):
        pendown()
        forward(sirka)
        left(90)
        forward(vyska)
        left(uhel)
        forward(strecha)
        left(uhel-180)
        forward(strecha)
        left(uhel)
        forward(vyska)
        left(uhel)
        forward(sirka)
        left(uhel)
        forward(odvesna)
        left(uhel)
        forward(vyska)
        left(uhel)
        forward(odvesna)
        left(135)
        penup()         
        forward(mezera)
        pendown() 

vykresli_domecek(20,30)
#vykresli_domecek(40)
#vykresli_domecek(80)

exitonclick()