from random import choice
tah_hrace = input("Kámen, nůžky, papír? :")
moznosti = ["kámen", "nůžky", "papír"]
tah_pocitace = choice(moznosti)
print(tah_pocitace)

if tah_hrace == "kámen":
    if tah_pocitace == "kámen":
        print("Remíza!")
    elif tah_pocitace == "nůžky":
        print("Vyhrál jsi!")
    else:
        print("Prohrál jsi!")

elif tah_hrace == "nůžky": 
    if tah_pocitace == "kámen":
        print("Prohrál jsi!")
    elif tah_pocitace == "nůžky":
        print("Remíza!")
    else:
        print("Vyhrál jsi!")

elif tah_hrace == "papír":
    if tah_pocitace == "kámen":
       print("Vyhrál jsi!")
    elif tah_pocitace == "nůžky":
        print("Prohrál jsi!")
    else:
        print("Remíza")

else: 
    print("Omlouvám se, znám pouze slova - kámen, nůžky, papír.")