print("                         CONVERSÃO DE METROS P/ KM, CM ou MM                         ")

meters = float(input("Digite a distância em metros: "))
print("Informe a unidade de medida escolhida. ")
conversion = input("centímetros (cm), quilômetros (km) ou milímetros (mm): ").strip().lower()

if conversion == "cm":
    result = meters * 100
    unit = "centímetros"
    abbreviation = "cm"

elif conversion == "km":
    result = meters / 1000
    unit = "quilômetros"
    abbreviation = "km"

elif conversion == "mm":
    result = meters * 1000
    unit = "milímetros"
    abbreviation = "mm"

else:
    print("Erro: Digite novamente distância e unidade")
    exit()

print(f"A distância digitada em metros é de {meters:.2f} metros convertendo para {unit} ficou {result:.2f}{abbreviation} ")