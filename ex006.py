print("         2026 ANO NOVO - SALARIO NOVO ")
print("Para saber seu aumento nos informo seu salario bruto: ")

salary = float(input("SALARIO ANTIGO: "))

if salary < 1200:
    print("Este valor não é valido ")
    exit()

if salary <= 2000:
    new_salary = salary * 1.15

elif salary > 2000 and salary <= 5000:
    new_salary = salary * 1.10

else:
    new_salary = salary * 1.05

print(f"Seu salario antigo era {salary:.2f} passou para {new_salary:.2f} ")

