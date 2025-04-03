print("Nakreslí obvod čtverce z pismene X - 5x5 \n")

for radek in range(7):
    if radek in (1, 6):
        print("X " * 6) 

    elif radek in range(2,6):
        print("X"+ 9*" "+"X")