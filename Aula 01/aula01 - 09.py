# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo 
# usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

quantidadeDias = int(input("Por quantos dias o carro foi alugado? "))
quantidadeKm = float(input("Quantos quilometros foram rodados? "))

valorDiarias = quantidadeDias * 60
valorQuilometragem = quantidadeKm * 0.15
valorTotal = valorDiarias + valorQuilometragem

print(f"O valor total das diárias é de R$ {valorDiarias:.2f}")
print(f"O valor total por kilometros rodados é de R$ {valorQuilometragem:.2f}")
print(f"Valor total a ser pago é de R$ {valorTotal:.2f}")