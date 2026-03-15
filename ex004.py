print("        CALCULO IMC        ")
weight = float(input("DIGITE SEU PESO: "))
height = float(input("DIGITE SUA ALTURA: "))

if height == 0:
    print("Altura não pode ser 0")
    exit()

imc = weight / (height ** 2)

if imc < 18.5:
    print(f"Abaixo do peso {imc:.2f} ")

elif 18.5 <= imc <= 24.9:
    print(f"Peso Ideal {imc:.2f} ")

else:
    print(f"Sobrepeso {imc:.2f} ")