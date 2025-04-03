rychlost = float(input("Vlož rychlost své chůze: "))

if rychlost >= 7:
    print("Toto již není chůze, ale běh.")
elif rychlost >= 6:
    print("Spěchej pomalu.")
elif rychlost >= 4:
    print("Pohoda, klídek ... vytrvej.")
elif rychlost >= 1: 
    print("Telefonuješ nebo jdeš s dětmi? Šnek se blíží.")
elif rychlost >= 0:
    print("Stojíš nebo jsi se zasekl.")
else:
    print("Návrat do minulosti? ")