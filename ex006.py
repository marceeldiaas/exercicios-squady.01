print("         2026 ANO NOVO - SALARIO NOVO ")
print("Para saber seu aumento nos informo seu salario bruto: ")
sal = float(input("SALARIO ANTIGO: "))

if sal <= 2000:
    nsal = sal * 1.15
    print(f"Seu salario antigo era {sal:.2f} passou para {nsal:.2f} ")

elif 2000 <= sal <= 5000:
    nsal = sal * 1.10
    print(f"Seu salario antigo era {sal:.2f} passou para {nsal:.2f} ")

else:
    nsal = sal * 1.05
    print(f"Seu salario antigo era {sal:.2f} passou para {nsal:.2f} ")

