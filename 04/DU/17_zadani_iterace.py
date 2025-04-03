# Upravená násobilka
print("1. Vypíšu ti násobilku \n")

nasobek = int(input("Zadej nejvyšší číslo, pro které chceš počítat násobky: "))

for sloupec in range(nasobek + 1):
    for radek in range(nasobek + 1):
               print(sloupec*radek, end=" ")
    print('\n')


# Upravený trojuhelník
print(3*'\n')
print("2. Trojúhelník z písmena X \n")

pocet = int(input("Zadej jak velká bude strana - počet X: "))

for i in range(1, pocet + 1): 
    print("X" * i) 


# Upravený "první řádek"
# Asi bych tam na řádku určeném uživatelem vypisovala něco jiného, ať 
# to není divné, že na 3. řádku je napsáno první řádek :-)
print(3*'\n')
print("3. Označí, který řádek je první \n")

cislo_radku = int(input("Zadej na kolikátém z 5ti řádku má program napsat 'první řádek':  "))
if cislo_radku > 5:
    print("Program vypisuje maximálně 5 řádků") 
else:
    for i in range(5): 
        if i == cislo_radku -1:
            print("první řádek") 
        else:
            print("není první")


# Upravený X obvod čtverce (cv.16)
print(3*'\n')
print("4. Nakreslí obvod čtverce z pismene X \n")

strana = int(input("Zadej kolik X má obsahovat strana čtverce: "))

for radek in range(strana + 1):
    if radek in (1, strana):
        print("X " * (strana)) 

    elif radek in range(2,strana):
        print("X"+ (2*strana-3)*" " + "X")