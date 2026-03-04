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
elif ((dia >= 20 and dia <= 30) and (mes == "abril")) or ((dia <= 20 and dia > 0) and (mes == "mayo")):
    print(nombre, " eres Aries, signo de fuego, enérgico y líder.")

# condicional para Geminis
elif ((dia >= 21 and dia <= 31) and (mes == "mayo")) or ((dia <= 20 and dia > 0) and (mes == "junio")):
    print(nombre, " eres Aries, signo de fuego, enérgico y líder.")

# condicional para Cancer
elif ((dia >= 21 and dia <= 30) and (mes == "junio")) or ((dia <= 22 and dia > 0) and (mes == "julio")):
    print(nombre, " eres Aries, signo de fuego, enérgico y líder.")

# condicional para Leo
elif ((dia >= 23 and dia <= 31) and (mes == "julio")) or ((dia <= 22 and dia > 0) and (mes == "agosto")):
    print(nombre, " eres Aries, signo de fuego, enérgico y líder.")

# condicional para Virgo
elif ((dia >= 23 and dia <= 31) and (mes == "agosto")) or ((dia <= 22 and dia > 0) and (mes == "septiembre")):
    print(nombre, " eres Aries, signo de fuego, enérgico y líder.")

# condicional para Libra
elif ((dia >= 23 and dia <= 30) and (mes == "septiembre")) or ((dia <= 22 and dia > 0) and (mes == "octubre")):
    print(nombre, " eres Aries, signo de fuego, enérgico y líder.")

    # condicional para Escorpio
elif ((dia >= 23 and dia <= 31) and (mes == "octubre")) or ((dia <= 21 and dia > 0) and (mes == "noviembre")):
    print(nombre, " eres Aries, signo de fuego, enérgico y líder.")

# condicional para Sagitario
elif ((dia >= 22 and dia <= 30) and (mes == "noviembre")) or ((dia <= 21 and dia > 0) and (mes == "diciembre")):
    print(nombre, " eres Aries, signo de fuego, enérgico y líder.")

# condicional para Capricornio
elif ((dia >= 22 and dia <= 31) and (mes == "diciembre")) or ((dia <= 20 and dia > 0) and (mes == "enero")):
    print(nombre, " eres Aries, signo de fuego, enérgico y líder.")

# condicional para Acuario
elif ((dia >= 21 and dia <= 31) and (mes == "enero")) or ((dia <= 19 and dia > 0) and (mes == "febrero")):
    print(nombre, " eres Aries, signo de fuego, enérgico y líder.")

# condicional para Piscis
elif ((dia >= 20 and dia <= 29) and (mes == "febrero")) or ((dia <= 20 and dia > 0) and (mes == "abril")):
    print(nombre, " eres Aries, signo de fuego, enérgico y líder.")

# condicion si los datos no existen
else:
    print("La fecha y/o el mes que ingresaste no son compatibles.")
