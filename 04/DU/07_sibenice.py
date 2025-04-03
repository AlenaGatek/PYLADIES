from random import choice 

vyber= ["trávník", "stromek", "stavení"]
slovo = choice(vyber)
sibenice = "_" * len(slovo)
uprava = 0

print(f'Ahoj, pojď si semnou zahrát šibenici. \nHádej slovo: {sibenice}')

pismeno = input(f'Prosím, hádej písmeno: ')
pismeno_lower = pismeno.lower()

if pismeno_lower in slovo:
    pozice = []
    for index, znak in enumerate(slovo):
        if znak == pismeno_lower:            
            sibenice[index] = pismeno_lower
            print(f'Písmeno "{pismeno_lower}" se nachází na pozicích: {[i for i, z in enumerate(slovo) if z == pismeno_lower]}')
            print(f'Aktuální stav slova: {"".join(sibenice)}')
        else:
            print(f'Písmeno "{pismeno_lower}" se ve slově nenachází.')
