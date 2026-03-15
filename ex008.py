try:
    print("Digite os números p/ o calculo: ")
    number1 = float(input("Número 1: "))
    number2 = float(input("Número 2: "))
    option = input("Qual operador vamos utilizar: +, -, *, / ").strip()

    if option not in ["+","-","*","/"]:
        print("Operador invalido! ")
        exit()

    if option == "/" and number2 == 0:
        print("Erro: Não é possível dividir por zero!")
        exit()

    if option == "+":
        result = number1 + number2
        choice = "soma"

    elif option == "-":
        result = number1 - number2
        choice = "subtração"

    elif option == "*":
        result = number1 * number2
        choice = "multiplicação"

    elif option == "/":
        result = number1 / number2
        choice = "divisão"

    print(f"A {choice} entre {number1} {option} {number2} é igual a {result:.2f}")

except ZeroDivisionError:
    print("Operador invalido! ")


