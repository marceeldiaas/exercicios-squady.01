print("------------ BEM-VINDO ------------" )
login = str(input("LOGIN: "))
senha = str(input("SENHA: "))

if login == "admin" and senha == "1234":
    print("ACESSO LIBERADO")

elif login == "admin":
    print("SENHA INCORRETA")

else:
    print("ACESSO NEGADO")