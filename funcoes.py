from math import pi, sin, cos
vLuz = 3 * 10 ** 8

# f = 1\ t              t-> período.
# k = 2pi/ comprimento  k-> perído.
# 

# retorna as variáveis com a entrada da frequência de onda
def freqInput(freq):
    comprimento = vLuz / freq
    
    k = 2 * pi / comprimento
    
    w = 2 * pi * freq
    
    return comprimento, k, w

# retorna as variáveis com a entrada do comprimento de onda
def compriInput(compri):
    freq = vLuz / compri
    
    k = 2 * pi / compri
    
    w = 2 * pi * freq
    
    return freq, k, w

