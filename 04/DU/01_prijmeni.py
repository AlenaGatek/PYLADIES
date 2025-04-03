print("Zjistím, zda jsi žena nebo muž podle nejtypičtějších znaků tvého jména.")

prijmeni = input("Zadej své příjemní: ")
koncovka_ova = prijmeni[-3:]
koncovka_a = prijmeni[-1:]

if koncovka_ova == "ová" or koncovka_ova == "ova" or koncovka_a == "á":
    print("S největší pravděpodobností jsi žena.")

else:
    print("S největší pravděpodobností jsi muž.")