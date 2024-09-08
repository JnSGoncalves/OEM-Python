from math import pi, sin, cos
vLuz = 3 * 10 ** 8
h = 4.135667696e-15  # Constante de Planck em eV·s
e = 1.602176634e-19  # Carga do elétron 

# f = 1\ t              t-> período.
# k = 2pi/ comprimento  k-> perído.
# 


def freqInput(freq):
    comprimento = vLuz / freq
    
    k = 2 * pi / comprimento
    
    w = 2 * pi * freq
    
    return comprimento, k, w

def comprimentoInput(comprimento):
    f = vLuz / comprimento
    k = 2 * pi / comprimento
    w = 2 * pi * f

    return f, k, w

def nOndaInput(k):

    comprimento = (2*pi)/k
    f = vLuz / comprimento
    w = 2*pi * f

    return comprimento, f, w

def freqAngInput(w):
    f = w/(2*pi)
    comprimento = vLuz / f
    k = 2 * pi / comprimento

    return comprimento, f, k