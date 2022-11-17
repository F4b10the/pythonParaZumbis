# Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado 
# a um milhão


# Faz o python exceder o limite de contagem
import sys
sys.set_int_max_str_digits(0)

print(len(str(2**1000000)))