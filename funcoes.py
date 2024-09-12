from math import pi, sin, cos, sqrt
vLuz = 3 * 10 ** 8
h = 4.135667696e-15  # Constante de Planck em eV·s
e = 1.602176634e-19  # Carga do elétron 
u = 4 * pi * 10 ** -7 # Constante Magnética em H/m


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

def emInput(em):
    bm = em / vLuz
    intensidade = vLuz / (2 * u) * (bm ** 2)
    
    return bm, intensidade

def intensidadeInput(intensidade):
    bm = sqrt((intensidade * (2 * u)) / vLuz)
    em = vLuz * bm

    return bm, em
  
def bmInput(bm):
    em = vLuz * bm
    intensidade = vLuz / (2 * u) * (bm ** 2)
    
    return em, intensidade


def tabelaConversoes():
    print("de rad/s -> rad/m = W(frequência angular)/Vluz = W/3x10^8")
    print()
    print("nm -> m  = nm * E-9")
    print("m -> nm = m * E+9")
    print()
    print("mc -> m  = mc * E-6")
    print("m -> mc = m * E+6")   
    print()
    print("Hz -> mHz = Hz * E-6")
    print("mHz -> Hz = mHz * E+6")
    print()