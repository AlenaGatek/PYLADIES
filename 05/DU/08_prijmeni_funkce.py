print("Vypíše u některých jmen jakého je jejich nositel pohlaví")

def prijmeni(zadane_prijmeni):
    koncovka_ova = zadane_prijmeni[-3:]
    koncovka_a = zadane_prijmeni[-1:]

    if koncovka_ova == "ová" or koncovka_ova == "ova" or koncovka_a == "á":
        return print(f"{zadane_prijmeni}: S největší pravděpodobností jsi žena.")
    else:
        return print(f"{zadane_prijmeni}: S největší pravděpodobností jsi muž.")

prijmeni("Nováková")
prijmeni("Novák")
prijmeni("Svobodova")
prijmeni("Svoboda")


