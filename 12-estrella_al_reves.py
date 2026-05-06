num = int(input("Pirámide de emojis, ingrese el número máximo: "))
for i in range(num, 0, -1):
    print("⭐" * i, end="")
    print("")