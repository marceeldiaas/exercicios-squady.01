print("Informe o tamanho das três medidas: ")
side_1 = float(input("medida 1: "))
side_2 = float(input("medida 2: "))
side_3 = float(input("medida 3: "))

if side_1 + side_2 > side_3 and side_1 + side_3 > side_2 and side_2 + side_3 > side_1:
    print("SIM! essas medidas formam um triângulo ")

    if side_1 == side_2 == side_3:
        print("É um triângulo equilátero ")

    elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
        print("É um triângulo isósceles ")

    else:
        print("É um triângulo escaleno ")

else:
    print("NÃO! essas medidas não formam um triângulo ")