# Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a 
# quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante 
# perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o 
# total de dias.

cigarrosPorDia = int(input("Quantos cigarros sao fumados por dia? "))
quantidadeAnos = int(input("Fumou por quantos anos? "))

totalDeCigarros = quantidadeAnos * 365 * cigarrosPorDia
tempoReduzidoEmMinutos = totalDeCigarros * 10
tempoReduzidoEmDias = tempoReduzidoEmMinutos / 1440

print(f"total De Cigarros, {totalDeCigarros}")
print(f"tempoReduzidoEmDias, {tempoReduzidoEmDias}")
print(f"tempoReduzidoEmMinutos, {tempoReduzidoEmMinutos}")

print (f"A quantidade de dias perdidos foi de {round(tempoReduzidoEmDias)} dias!")
