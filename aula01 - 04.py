#  Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a 
# porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input("Informe seu salário atual: "))
percentual = float(input("Informe a porcentagem do aumento: "))

aumento = salario * percentual / 100 + salario

print (f"O valor do salario de R$ {salario:.2f}, com o aumento de {percentual:.2f}%, passará a ser de R${aumento:.2f}")