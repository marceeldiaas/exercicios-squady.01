num = int(input("Digite um número: "))
result = num % 2

if result.isdigit():
    print("Código invalido")

elif num < 0:
    print("Código invalido ")

elif result == 0:
    print(f"PAR: {num}")

else:
    print(f"IMPAR: {num}")