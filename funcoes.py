from math import pi, sin, cos
vLuz = 3 * 10 ** 8

# f = 1\ t              t-> período.
# k = 2pi/ comprimento  k-> perído.
# 


def freqInput(freq):
    comprimento = vLuz / freq
    
    k = 2 * pi / comprimento
    
    w = 2 * pi * freq
    
    return comprimento, k, w