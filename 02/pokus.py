from random import randrange
cislo = randrange(0, 3)
print(cislo)

if cislo == 0:
    tvar = 'trojúhelník'
elif cislo == 1:
    tvar = 'čtverec'
else:
    tvar = 'kolečko'

print(tvar)