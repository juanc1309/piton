n = int(input("\n\nDame un número máximo para la cuenta regresiva: "))
for i in range(n,-1,-1):
    print(i)
print("""


""")

num = int(input("Pirámide de emojis, ingrese el número máximo: "))
for i in range(1,num):
    for j in range(0,i):
        print("#" * i)
    print("")