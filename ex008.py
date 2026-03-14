print("Digite os números p/ o calculo: ")
n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
opcao = str(input("Qual operador vamos utilizar: +, -, *, / "))

if opcao == "+":
    res = n1 + n2
    print(f"A soma de {n1} + {n2} é igual a {res} ")

elif opcao == "-":
    res = n1 - n2
    print(f"A subtração de {n1} - {n2} é igual a {res} ")

elif opcao == "*":
    res = n1 * n2
    print(f"A multiplicação de {n1} * {n2} é igual a {res:.2f} ")

elif opcao == "/" and n2 == 0:
    print(f"Não é possível realizar este calculo matematico! ")

elif opcao == "/":
    res = n1 / n2
    print(f"A divisão entre {n1} / {n2} é igual a {res:.2f}")

else:
    print("Operador invalido! ")

