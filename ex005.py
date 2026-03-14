print("     MENTORIA SQUADY ACADEMY    ")
print("Por favor informe suas notas: ")
n1 = float(input("NOTA 1: "))
n2 = float(input("NOTA 2: "))
n3 = float(input("NOTA 3: "))

media = (n1 + n2 + n3) / 3

if media >= 7:
    print(f"PARABENS SUA MEDIA FOI DE {media:.2f} VOCÊ ESTÁ APROVADO")

elif 5 <= media <= 6.9:
    print(f"SUA MEDIA FOI DE {media:.2f} VOCÊ ESTÁ DE RECUPERAÇÃO")

else:
    print(f"SUA MEDIA FOI DE {media:.2f} VOCÊ ESTÁ REPROVADO")