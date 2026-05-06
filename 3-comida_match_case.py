# Código con match case :-)
comida_vergas = int(input("\n¿Qué hora es bro? "))
match comida_vergas:
    case 8:
        print("Es hora de desayunar")
    case 14:
        print("Es hora de comer")
    case 21:
        print("Es hora de cenar")
    case _:
        print("No es hora de comer bro")
