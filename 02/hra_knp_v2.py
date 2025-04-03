from random import choice

tah_hrace = input("Kámen, nůžky, papír? :")
moznosti = ["kámen", "nůžky", "papír"]
tah_pocitace = choice(moznosti)
print(tah_pocitace)

if tah_pocitace == tah_hrace:
    print("Remíza!")

elif (tah_pocitace == "nůžky" and tah_hrace == "kámen") or \
     (tah_pocitace == "kámen" and tah_hrace == "papír") or \
     (tah_pocitace == "papír" and tah_hrace == "nůžky"):
    print("Vyhrál jsi!")

elif (tah_pocitace == "nůžky" and tah_hrace == "papír") or \
     (tah_pocitace == "kámen" and tah_hrace == "nůžky") or \
     (tah_pocitace == "papír" and tah_hrace == "kámen"):
    print("Počítač vyhrál!")

else:
    print("Omlouvám se, znám pouze slova - kámen, nůžky, papír.")