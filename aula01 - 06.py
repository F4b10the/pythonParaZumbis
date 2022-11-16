# Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média 
# esperada para a viagem

distancia = float(input("Qual a distancia total a ser percorrida em Km? " ))
velocidade = float(input("Qual será a velocidade média empregada em Km/h? "))

tempoMedio = distancia / velocidade


print(f"O tempo médio para o fim do percurso é de {tempoMedio:.2f} horas")


