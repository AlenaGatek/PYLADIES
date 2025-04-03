def pruzkum(hloubka):
    print(f'Rozhlížím se v hloubce {hloubka} m')

    if hloubka >= 30:
        print('Už toho bylo dost!')
    else:
        print(f'Zanořuju se (z {hloubka} m)')

        pruzkum(hloubka + 10)

        print(f'Vynořuju se (na {hloubka} m)')

pruzkum(0)