print("        CALCULO IMC        ")
peso = float(input("DIGITE SEU PESO: "))
altura = float(input("DIGITE SUA ALTURA: "))
imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso")

elif 18.5 <= imc <= 25:
    print("Peso Ideal")

else:
    print("Sobrepeso")