# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule 
# o total em segundos.

dias = int(input("Informe quantos dias: "))
horas = int(input("Informe quantas horas: "))
minutos = int(input("Informe quantos minutos: "))
segundos = int(input("Informe quantos segundos: "))

diasEmSegundos = dias * 86400
horasEmSegundos = horas * 3600
minutosEmSegundos = minutos * 60
segundosTotais = diasEmSegundos + horasEmSegundos + minutos + segundos


print(f'A quantidade de segundos contida em {dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos, é de {segundosTotais} segundos')