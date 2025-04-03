from turtle import speed, forward, right, goto, penup, pendown, done, exitonclick
from random import randrange, randint

print("Podívej se na nebe, kolik je tam hvězd? ZPOČÍTEJ JE!!!")

speed(10)
pocet_hvezd = randrange(5,20)#náhodně vybere, kolik hvězd se nakreslí

for h in range(pocet_hvezd):

    velikost = randrange(10, 80) #velikost hvězdy
    for i in range(5):  
        forward(velikost)
        right(144) 

    penup()   
    x = randint(-300, 300)
    y = randint(-300, 300)
    goto(x, y)
    pendown()

exitonclick()

odpoved = int(input("Kolik jsi napočítal hvězd?: "))

if odpoved == pocet_hvezd:
    print("Správně, rozzářilo se ti přesně tolik hvězd.")

else:
    print("To ne...Tolik hvězd ti štěstí nepřinese.")