print("Porovnej dvě čísla")
prvni_cislo = int(input("První číslo: "))
druhe_cislo = int(input("Druhé číslo: "))

if prvni_cislo > druhe_cislo:
    print("Číslo ", prvni_cislo, "je větší než číslo ", druhe_cislo)

elif prvni_cislo < druhe_cislo:
    print("Číslo ", prvni_cislo, "je menší než číslo ", druhe_cislo)

else:
    print("Čísla jsou si rovna")