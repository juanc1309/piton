# título
print("Veamos tu horóscopo")
# ingreso de datos
nombre = input("Ingrese su nombre: ")
dia = int(input("Ingrese su día de nacimiento: "))
mes = input("Ingrese su mes de nacimiento (En minúsculas todo el texto): ")
# condicional para Aries
if ((dia >= 21 and dia <= 31) and (mes == "marzo")) or ((dia <= 19 and dia > 0) and (mes == "abril")):
    print(nombre, " eres Aries, signo de fuego, enérgico y líder.")
# condicional para Tauro
elif ((dia >= 20 and dia <= 31) and (mes == "abril")) or ((dia <= 19 and dia > 0) and (mes == "abril")):
    print(nombre, " eres Aries, signo de fuego, enérgico y líder.")