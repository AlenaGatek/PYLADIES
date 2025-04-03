from turtle import forward, left, exitonclick

print("Tento program ti vykreslí ornament - jednoduché čtvercové bludiště.")

delka = 0

for i in range(20):
    forward(delka)
    left(90)
    delka = delka + 10
    
exitonclick()
