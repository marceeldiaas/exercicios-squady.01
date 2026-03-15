print("     MENTORIA SQUADY ACADEMY    ")
print("Por favor informe suas notas: ")

proof_1 = float(input("NOTICE 1: "))
proof_2 = float(input("NOTICE 2: "))
proof_3 = float(input("NOTICE 3: "))

if (proof_1 < 0 or proof_1 > 10) or (proof_2 < 0 or proof_2 > 10) or (proof_3 < 0 or proof_3 > 10):
    print("Digite um número entre 0 e 10 ")
    exit()

media = (proof_1 + proof_2 + proof_3) / 3

if media >= 7:
    situation = "APROVADO"

elif 5 <= media < 7:
    situation = "RECUPERAÇÃO"

else:
    situation = "REPROVADO"

print(f"NOTA 1: {proof_1} | NOTA 2: {proof_2} | NOTA 3: {proof_3} | MÉDIA {media:.2f} | SITUAÇÃO: {situation} ")
