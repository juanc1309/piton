for i in range(10):
    print("La secencia es: ", i)

for i in range(50, 2):
    print("Con 2 argumento: ", i)

for i in range(10, 50, 2):
    print("Con 3 argumentos: ", i)

# Pide el número máximo al usuario para que haga una cuenta regresiva

n = int(input("\n\nDame un número máximo para la cuenta regresiva: "))
for i in range(n,0,-1):
    print(i)