def calcular_inss(salario_bruto):
    if salario_bruto <= 1100:
        return salario_bruto * 0.075
    elif 1100.01 <= salario_bruto <= 2203.048:
        return salario_bruto * 0.99
    elif 2203.049 <= salario_bruto <= 3305.22:
        return salario_bruto * 0.12
    elif 3305.23 <= salario_bruto <=6433.57:
        return salario_bruto * 0.14
    else:
        return 751.99

def calcular_irrf(salario_liquido):
    if salario_liquido <= 1903.98:
        return 0
    elif 1903.99 <= salario_liquido <= 2826.65:
        return (salario_liquido * 0.075) - 142.8
    elif 2826.66 <= salario_liquido <= 3751.05:
        return (salario_liquido * 0.15) - 354.8
    elif 3751.06 <= salario_liquido <=4664.68:
        return (salario_liquido * 0.225) - 636.13
    else:
        return (salario_liquido * 0.275) - 869.36
    
def calcular_hora_extra(salario_bruto, horas_extras_trabalhadas):
    valor_hora = salario_bruto / 220
    adicional = valor_hora * 0.5
    return horas_extras_trabalhadas * (valor_hora + adicional)

salario_bruto = float(input("Digite o salário bruto do funcionario: R$ "))
horas_extra = int(input("Digite a quantidade de horas extras trabalhadas no mêS: "))

desconto_inss = calcular_inss(salario_bruto)

salario_liquido = salario_bruto - desconto_inss

desconto_irff = calcular_irrf(salario_liquido)

provento_horas_extra = calcular_hora_extra(salario_bruto, horas_extra)

salario_final = salario_liquido + provento_horas_extra - desconto_irff

print("\n*** Folha de salario ***")
print(f"Salario bruto: R$ {salario_bruto:.2f}")
print(f"Provento Horas Extras: R$ {provento_horas_extra:.2f}")
print(f"Desconto INSS: R$ {desconto_inss:.2f}")
print(f"Desconto IRRF: R$ {desconto_irff:.2f}")
print("-------------------------------")
print(f"Salario Final: R$ {salario_final:.2f}")