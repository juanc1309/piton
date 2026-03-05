print("Resolviendo una ecuación de primer grado")
a = int(input("Ingrese el coeficiente A: "))
while a == 0:
    a = int(input("Ingrese un número diferente a cero en el coeficiente A: "))
b = int(input("Ingrese el coficiente B: "))
r = (-1 * b) / a
print(r)