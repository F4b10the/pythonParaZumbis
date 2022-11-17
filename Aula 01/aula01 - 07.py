#  Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32

temperatura = float(input("Qual a temperatura, em celsius, a ser convertida? "))

fahrenheit = temperatura * 1.8 + 32

print(f"A temperatura informada, em farenheit, é de {fahrenheit:.2f}°")