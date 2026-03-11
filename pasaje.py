print("************************")
print("*    Buses El Pitón    *")
print("************************")
print("")
print("Buses El Pitón ofrece distintos viajes a varios puntos del país.")
print("1. Monterrey  $950")
print("2. Guadalajara $850")
print("3. Cancún $1200")
destino = int(input("Ingrese el número del destino que desea ir: "))
edad = int(input("Ingrese su edad: "))
match destino:
    case 1:
        destino = 950
    case 2:
        destino = 850
    case 3:
        destino = 1200
if edad >= 0 and edad <= 3:
    print("No paga pasaje")
elif edad >= 4 and edad <= 11:
    edad = 0.5
    print("Pagara $", edad * destino)
elif edad >= 12 and edad <= 17:
    edad = 0.7
    print("Pagara $", edad * destino)
elif edad >= 18 and edad <= 59:
    edad = 1
    print("Pagara $", edad * destino)
elif edad >= 60:
    edad = 0.8
    print("Pagara $", edad * destino)