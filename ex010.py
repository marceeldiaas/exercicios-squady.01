money = int(input("Informe o valor que deseja sacar: "))

value50 = value20 = value10 = 0

if money >= 50:
    value50 = money / 50
    money = value50 % 50

if money >= 20:
    value20 = money / 20
    money = valeu20 % 20

if money >= 10:
    value10 = money / 10
    money = valeu10 % 10

if value50 > 0:
    print(f"Notas de 50 {value50} ")

if value20 > 0:
    print(f"Notas de 20 {value20} ")

if value10 > 0:
    print(f"Notas de 10 {value10} ")

if money > 0:
    print(f"Sobrou o valor de {money} ")