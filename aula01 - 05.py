# Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o 
# preço a pagar.

mercadoria = float(input("Informe o preço da mercadoria: "))
desconto = float(input("Informe o percentual do desconto: "))

valorComDesconto = mercadoria - (desconto * mercadoria / 100)

print (f"Valor da mercadoria: R${mercadoria}")
print (f"Valor do desconto: {desconto}%")
print (f"Valor atualizado: R${valorComDesconto:.2f}")
