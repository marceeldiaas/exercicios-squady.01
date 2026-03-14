print("Informe o tamanho das três medidas: ")
med1 = int(input("medida 1: "))
med2 = int(input("medida 2: "))
med3 = int(input("medida 3: "))

if med1 + med2 > med3 and med1 + med3 > med2 and med2 + med3 > med1:
    print("SIM! essas medidas formam um triângulo ")

    if med1 == med2 == med3:
        print("É um triângulo equilátero ")

    elif med1 == med2 or med1 == med3 or med2 == med3:
        print("É um triângulo isósceles ")

    else:
        print("É um triângulo escaleno ")

else:
    print("NÃO! essas medidas não formam um triângulo ")