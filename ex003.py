print("------------ BEM-VINDO ------------" )

username = input("LOGIN: ").strip().lower()
password = input("SENHA: ")

if  username == "admin" and password == "1234":
    permission = "LIBERADO"

elif username == "admin":
    permission = "NEGADO"

else:
    print("Usuário não reconhecido. Acesso negado ")
    exit()

print(f"Acesso: {permission} ")