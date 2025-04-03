prvni_cislo = int(input("První číslo: "))
druhe_cislo = int(input("Druhé číslo: "))
operace = input("Operace: ")
operatory = ["+", "-", "/", "*"]

if operace == "+":
   print(prvni_cislo, " + ", druhe_cislo, " = ", prvni_cislo + druhe_cislo)

elif operace == "-":
    print(prvni_cislo, " - ", druhe_cislo, " = ", prvni_cislo - druhe_cislo)
    
elif operace == "/" and druhe_cislo == 0:
    print("Nulou dělit nelze")

elif operace == "/":
    print(prvni_cislo, " / ", druhe_cislo, " = ", prvni_cislo / druhe_cislo)

elif operace == "*":
    print(prvni_cislo, " * ", druhe_cislo, " = ", prvni_cislo * druhe_cislo)

else: 
    print("Zadejte prosím jeden z těchto operátorů:", operatory)