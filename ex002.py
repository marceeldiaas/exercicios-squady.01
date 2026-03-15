try:
    print("Digite dois números: ")
    n1 = float(input("NÚMERO 1: "))
    n2 = float(input("NÚMERO 2: "))

    if n1 == n2:
        print("Números são iguais ")

    elif n1 > n2:
        print(f"MAIOR: {n1}")

    else:
        print(f"MAIOR: {n2}")

except ValueError:
    print("Use apenas números inteiros")

