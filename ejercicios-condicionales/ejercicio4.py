name = input("¿Cómo te llamas? ")
sexo = input("¿Cuál es tu sexo (M o H)? ")
if sexo == "M":
    if name.lower() < "m":
        group = "A"
    else:
        group = "B"
else:
    if name.lower() > "n":
        group = "A"
    else:
        group = "B"
print("Tu grupo es " + group)