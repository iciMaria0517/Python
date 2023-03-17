age = int(input("¿Cuál es tu edad? "))
income = float(input("¿Cuales son tus ingresos mensuales?"))
if age > 16 and income >= 1000:
    print("Tienes que tributar")
else:
    print("No tienes que tributar")